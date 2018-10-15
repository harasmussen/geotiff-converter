# Geotiff Converter
## Intoduction

For [this sun simulating project](http://www.rapidolabs.dk/sun) I had to import height data from public databases which was encoded in geotiff files. Luckily the people over GDAL have implemented import functionalities from geotiff files and [Ozak](https://github.com/ozak) have made nice python package called [`georasters`](https://github.com/ozak/georasters) that are abstracting out the complexities within `GDAL`. However, since I had problems installing `georasters` and `GDAL` on my Mac I decided to create a docker container that would convert the tiff files into `NumPy` binary files. These files seem more simple to load and the NumPy library is generally widely accessible.

## System Requirements
You should have docker installed on your system.

## Using the container
Clone this repository:
```
git clone https://github.com/harasmussen/geotiff-converter.git
cd geotiff-converter
```
Copy your tiff files into the data directory of the repository:
```
cp [path to your *.tif files] data
```
Then build and run the dockers:
```
docker build -t geotiff-converter
docker run -v $(pwd)/data:/usr/src/app/data geotiff-converter
```
The converted files should now be in the `data` folder.
