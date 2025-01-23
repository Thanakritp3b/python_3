import numpy as np
import matplotlib.pyplot as plt
import random
import time


def gen_segments():
    segments = np.random.uniform(0, 10, size=(500, 4))
    return segments.tolist() 

def is_rectangle(segments, rectangle):
    x_min, y_min, x_max, y_max = rectangle
    filtered = []

    for seg in segments:
        x1, y1, x2, y2 = seg
        if ( x_min <= x1 <= x_max and
             y_min <= y1 <= y_max and
             x_min <= x2 <= x_max and
             y_min <= y2 <= y_max ):
            filtered.append(seg)
    return filtered


def numpy_filter(segments, rectangle):
    segments_array = np.array(segments)
    x_min, y_min, x_max, y_max = rectangle 
    mask = ((segments_array[:, 0] >= x_min) & 
            (segments_array[:, 0] <= x_max) &
            (segments_array[:, 1] >= y_min) & 
            (segments_array[:, 1] <= y_max) &
            (segments_array[:, 2] >= x_min) & 
            (segments_array[:, 2] <= x_max) &
            (segments_array[:, 3] >= y_min) & 
            (segments_array[:, 3] <= y_max))
    return segments_array[mask].tolist()

def plot_graph(segments, filter, rectangle):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    for seg in segments:
        ax1.plot([seg[0], seg[2]], [seg[1], seg[3]], '-', alpha=0.5)
    ax1.set_title('All Lines')
    ax1.grid(True)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    
    for seg in filter:
        ax2.plot([seg[0], seg[2]], [seg[1], seg[3]], '-', alpha=0.5)
    ax2.set_title('Filtered Lines')
    ax2.grid(True)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    
    x_min, y_min, x_max, y_max = rectangle
    rect = plt.Rectangle((x_min, y_min), x_max-x_min, y_max-y_min,
                        fill=False, color='red', linestyle='--')
    ax2.add_patch(rect)
    
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    segments = gen_segments()
    rectangle = [2, 2, 8, 8]

    start_time = time.time()
    normal_filter = is_rectangle(segments, rectangle)
    end_time = time.time() - start_time
    print(f"normal : {end_time}")

    start_time = time.time()
    numpy_filter = numpy_filter(segments, rectangle)
    end_time = time.time() - start_time
    print(f"numpy filter : {end_time}")

    plot_graph(segments, normal_filter , rectangle)
            