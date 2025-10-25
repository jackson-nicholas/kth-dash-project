import os, time, subprocess, requests, matplotlib.pyplot as plt

# DASH 可用码率(kbps)
bitrates = [500, 1000, 2000]
current_bitrate = 1000

# 模拟不同网络场景 (rate, delay, loss)
net_conditions = [
    ("1mbit", "100ms", "1%"),
    ("2mbit", "80ms", "0%"),
    ("800kbit", "120ms", "2%"),
    ("3mbit", "60ms", "0%"),
    ("500kbit", "150ms", "5%"),
]

segments, measured_bw, selected_bitrate = [], [], []

print("Starting real network DASH simulation...\n")

for i, (rate, delay, loss) in enumerate(net_conditions, start=1):
    print(f"[{i}] Applying network: rate={rate}, delay={delay}, loss={loss}")
    subprocess.run(["tc", "qdisc", "del", "dev", "eth0", "root"], stderr=subprocess.DEVNULL)
    subprocess.run(["tc", "qdisc", "add", "dev", "eth0", "root", "netem",
                    "delay", delay, "loss", loss, "rate", rate])

    url = "https://speed.cloudflare.com/__down?bytes=1000000"
    start = time.time()
    r = requests.get(url)
    duration = time.time() - start
    bw = len(r.content) * 8 / 1000 / duration  # kbps

    # DASH 自适应决策
    if bw < current_bitrate * 0.8:
        new_br = max([b for b in bitrates if b <= bw], default=min(bitrates))
    elif bw > current_bitrate * 1.2 and current_bitrate < max(bitrates):
        new_br = min([b for b in bitrates if b >= bw], default=max(bitrates))
    else:
        new_br = current_bitrate

    print(f"→ Measured BW: {bw:.1f} kbps | bitrate {current_bitrate} → {new_br}\n")

    segments.append(i)
    measured_bw.append(bw)
    selected_bitrate.append(new_br)
    current_bitrate = new_br
    time.sleep(1)

# 清理 tc 设置
subprocess.run(["tc", "qdisc", "del", "dev", "eth0", "root"], stderr=subprocess.DEVNULL)

# 绘图
plt.figure(figsize=(8,4))
plt.plot(segments, measured_bw, 'o--', label='Measured bandwidth (kbps)')
plt.plot(segments, selected_bitrate, 's-', label='Selected bitrate (kbps)')
plt.xlabel("Test segment")
plt.ylabel("kbps")
plt.title("Real Network DASH Adaptation with tc netem")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("/workspace/videos/real_dash_result.png")
plt.show()

print("✅ Simulation finished — result saved as real_dash_result.png")
