import napari

from napari_command_palette import install

if __name__ == "__main__":
    viewer = napari.Viewer()
    install(viewer)
    napari.run()
