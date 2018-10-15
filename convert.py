# build and run this: 
# docker build . -t convert && docker run -v [path to repos]/data:/usr/src/app/data deploy


from pathlib import Path
import georasters as gr
import numpy as np

data_path = Path("data")
files = [f for f in data_path.iterdir() if f.suffix == ".tif"]

for f in files:
    print(f)
    data = gr.from_file(str(f))

    cell_size = data.x_cell_size
    height, width = data.raster.data.shape
    geo_and_meta_data = {
        'data': data.raster.data,
        'min_x': data.xmin,
        'max_x': data.xmax,
        'min_y': data.ymin,
        'max_y': data.ymax,
        'cell_size_x': data.x_cell_size,
        'cell_size_y': data.y_cell_size,
        'projection': data.projection.ExportToWkt()
    }
    out_file_path = (data_path / f.stem).with_suffix('.npz')

    np.savez(out_file_path, **geo_and_meta_data)