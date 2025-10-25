import time
import matplotlib.pyplot as plt

# 可用码率(kbps)
bitrates = [500, 1000, 2000]
current_bitrate = 1000

# 模拟片段大小 (bytes)
segment_sizes = {
    500: 4.5 * 1024 * 1024,
    1000: 8.1 * 1024 * 1024,
    2000: 15.1 * 1024 * 1024
}

# 模拟网络带宽序列 (kbps)
network_bandwidth = [600, 1500, 900, 2200, 400, 1800, 1000, 2500, 800, 1600]

segments = []
bitrates_used = []
bandwidths = []

print("Simulating adaptive DASH playback...\n")

for i, bw in enumerate(network_bandwidth):
    seg_size = segment_sizes[current_bitrate] * 8 / 1000  # bits→kb
    download_time = seg_size / bw

    # 自适应逻辑（带边界保护）
    if bw < current_bitrate * 0.8:
        new_bitrate = max([b for b in bitrates if b <= bw], default=min(bitrates))
    elif bw > current_bitrate * 1.2 and current_bitrate < max(bitrates):
        new_bitrate = min([b for b in bitrates if b >= bw], default=max(bitrates))
    else:
        new_bitrate = current_bitrate

    print(f"Segment {i+1}: bw={bw:4d} kbps | bitrate={current_bitrate} → {new_bitrate} | download={download_time:.2f}s")
    current_bitrate = new_bitrate

    segments.append(i + 1)
    bitrates_used.append(current_bitrate)
    bandwidths.append(bw)
    time.sleep(0.2)

print("\nSimulation finished — generating plot...")

# 绘制折线图
plt.figure(figsize=(8,4))
plt.plot(segments, bandwidths, 'o--', label='Network bandwidth (kbps)')
plt.plot(segments, bitrates_used, 's-', label='Selected bitrate (kbps)')
plt.xlabel('Segment number')
plt.ylabel('kbps')
plt.title('DASH Bitrate Adaptation Simulation')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('/workspace/videos/dash_result.png')
plt.show()
print("Plot saved to /workspace/videos/dash_result.png")
