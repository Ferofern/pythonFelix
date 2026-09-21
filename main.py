import imageio.v3 as iio
import numpy as np

input_video = "/workspaces/pythonFelix/has_que_mueva_la_boca_y_hablae.mp4"
output_video = "/workspaces/pythonFelix/sin_fondo.mp4"

frames = iio.imread(input_video)
meta = iio.immeta(input_video)
fps = meta.get('fps', 30)

output_frames = []

for frame in frames:
    rgba = np.dstack([frame, np.full(frame.shape[:2], 255, dtype=np.uint8)])
    
    lower_white = np.array([200, 200, 200, 0])
    upper_white = np.array([255, 255, 255, 255])
    
    mask = (rgba[:, :, 0] >= lower_white[0]) & \
           (rgba[:, :, 1] >= lower_white[1]) & \
           (rgba[:, :, 2] >= lower_white[2])
           
    rgba[mask] = [0, 0, 0, 0]
    output_frames.append(rgba)

iio.imwrite(
    output_video, 
    output_frames, 
    fps=fps, 
    codec='libvpx-vp9', 
    pixelformat='yuva420p'
)