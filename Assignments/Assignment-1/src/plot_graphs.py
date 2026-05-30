
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Your data
nodes = [1, 2, 3]
times = [42, 28, 23]
speedup = [1.00, 1.50, 1.82]
ideal_times = [42, 21, 14]  
ideal_speedup = [1, 2, 3]

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Execution Time
ax1.plot(nodes, times, 'bo-', linewidth=2.5, markersize=10, label='Actual Time')
ax1.plot(nodes, ideal_times, 'r--', linewidth=2, label='Ideal Linear Scaling')
ax1.set_xlabel('Number of Nodes', fontsize=12)
ax1.set_ylabel('Execution Time (seconds)', fontsize=12)
ax1.set_title('Scalability: Execution Time vs Cluster Size', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=11)
ax1.set_xticks(nodes)

# Add time labels on points
for i, (n, t) in enumerate(zip(nodes, times)):
    ax1.annotate(f'{t}s', (n, t), textcoords="offset points", 
                xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')

# Plot 2: Speedup
ax2.plot(nodes, speedup, 'go-', linewidth=2.5, markersize=10, label='Actual Speedup')
ax2.plot(nodes, ideal_speedup, 'r--', linewidth=2, label='Ideal Linear Speedup')
ax2.set_xlabel('Number of Nodes', fontsize=12)
ax2.set_ylabel('Speedup Factor', fontsize=12)
ax2.set_title('Speedup Analysis: Actual vs Ideal', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=11)
ax2.set_xticks(nodes)

# Add speedup labels
for i, (n, s) in enumerate(zip(nodes, speedup)):
    ax2.annotate(f'{s:.2f}x', (n, s), textcoords="offset points", 
                xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('scalability_graph.png', dpi=300, bbox_inches='tight')
plt.savefig('scalability_graph.pdf', bbox_inches='tight')
print(" Graphs saved as scalability_graph.png and scalability_graph.pdf")

# Create a bar chart for comparison
plt.figure(figsize=(10, 6))
x = np.arange(len(nodes))
width = 0.35

plt.bar(x - width/2, times, width, label='Execution Time', color='steelblue')
plt.bar(x + width/2, [42/i for i in nodes], width, label='Ideal Time', color='lightcoral', alpha=0.7)

plt.xlabel('Number of Nodes', fontsize=12)
plt.ylabel('Time (seconds)', fontsize=12)
plt.title('Execution Time Comparison: Actual vs Ideal', fontsize=14, fontweight='bold')
plt.xticks(x, ['1 Node', '2 Nodes', '3 Nodes'])
plt.legend()
plt.grid(True, alpha=0.3)

# Add value labels
for i, (t, it) in enumerate(zip(times, [42, 21, 14])):
    plt.text(i - width/2, t + 1, f'{t}s', ha='center', fontweight='bold')
    plt.text(i + width/2, it + 1, f'{it}s', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('comparison_bar_chart.png', dpi=300)
print("Bar chart saved as comparison_bar_chart.png")
