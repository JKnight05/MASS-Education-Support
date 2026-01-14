# Matplotlib: Data Visualization Capabilities

Matplotlib is Python's most popular plotting library, capable of creating publication-quality visualizations ranging from simple line plots to complex 3D graphics.

## Basic Setup

```python
import matplotlib.pyplot as plt
import numpy as np
```

## Core Capabilities

### 1. Line Plots
Perfect for time series, trends, and continuous data.

```python
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Trigonometric Functions')
plt.legend()
plt.grid(True)
plt.show()
```

### 2. Scatter Plots
Visualize correlations and distributions.

```python
x = np.random.randn(100)
y = 2*x + np.random.randn(100)
plt.scatter(x, y, alpha=0.5, c=y, cmap='viridis')
plt.colorbar(label='Y value')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

### 3. Bar Charts & Histograms
Compare categories or show distributions.

```python
# Bar chart
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
plt.bar(categories, values, color='steelblue')

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
plt.show()
```

### 4. Subplots
Create multiple plots in one figure.

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, np.sin(x))
axes[0, 1].scatter(x, np.cos(x))
axes[1, 0].bar(['A', 'B', 'C'], [1, 2, 3])
axes[1, 1].hist(np.random.randn(100))
plt.tight_layout()
plt.show()
```

### 5. Heatmaps
Display matrix data and correlations.

```python
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()
```

### 6. Pie Charts
Show proportions and percentages.

```python
sizes = [30, 25, 20, 25]
labels = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()
```

### 7. Customization Options
- **Colors**: Named colors, hex codes, colormaps (viridis, plasma, coolwarm, etc.)
- **Markers**: 'o', 's', '^', '*', '+', and more
- **Line styles**: '-', '--', '-.', ':'
- **Annotations**: Add text, arrows, and labels to specific points
- **Styles**: Use `plt.style.use('seaborn')` for different aesthetics

### 8. Advanced Features
- **3D Plots**: Using `mpl_toolkits.mplot3d`
- **Animations**: Create dynamic visualizations
- **Contour Plots**: Topographic-style visualizations
- **Error Bars**: Show uncertainty in data
- **Fill Between**: Shade areas under curves
- **Logarithmic Scales**: For exponential data

## Quick Tips for Projects

1. **Save Figures**: `plt.savefig('plot.png', dpi=300, bbox_inches='tight')`
2. **Interactive Mode**: Use `%matplotlib inline` in Jupyter notebooks
3. **Figure Size**: Set with `plt.figure(figsize=(10, 6))`
4. **Combine with Pandas**: DataFrames have built-in `.plot()` methods
5. **Seaborn Integration**: Built on matplotlib with easier statistical plots

## Resources
- Official Documentation: https://matplotlib.org/
- Gallery: https://matplotlib.org/stable/gallery/index.html
- Cheat Sheets: Search for "matplotlib cheat sheet" for quick references