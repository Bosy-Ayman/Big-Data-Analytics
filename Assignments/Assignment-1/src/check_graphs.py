#!/usr/bin/env python3
import os
import glob

print("=" * 50)
print("CHECKING GRAPH FILES")
print("=" * 50)

# Check if graphs were created
png_files = glob.glob("*.png")
pdf_files = glob.glob("*.pdf")

print(f"PNG files found: {len(png_files)}")
for f in png_files:
    size = os.path.getsize(f)
    print(f"  - {f} ({size} bytes)")

print(f"\nPDF files found: {len(pdf_files)}")
for f in pdf_files:
    size = os.path.getsize(f)
    print(f"  - {f} ({size} bytes)")

print("\n" + "=" * 50)

if "scalability_graph.png" in png_files:
    print("✅ scalability_graph.png exists")
else:
    print("❌ scalability_graph.png missing - run: python3 plot_graphs.py")

if "comparison_bar_chart.png" in png_files:
    print("✅ comparison_bar_chart.png exists")
else:
    print("❌ comparison_bar_chart.png missing - run: python3 plot_graphs.py")

print("=" * 50)


