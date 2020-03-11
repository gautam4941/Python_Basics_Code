path = []
import matplotlib.pyplot as plt

def pictures( **photos ):
    print( "Inside Pictures Functions" )
    print( f"Photos = { photos }" )
    print( f"len( photos ) = { len( photos ) }" )

    pixels = []
    for i in photos.values():
        pixels.append( plt.imread( i ) )

    print( pixels )

    for i in pixels:
        plt.imshow( i )
        plt.show()

path.append( r"C:\Users\gauta\PycharmProjects\OpenCV2\DataSets\peppers_color.tif" )
path.append( r"C:\Users\gauta\PycharmProjects\OpenCV2\DataSets\mandril_color.tif" )
path.append( r"C:\Users\gauta\PycharmProjects\OpenCV2\DataSets\cameraman.tif" )

print( f"path = { path }" )
print()

pictures( img1 = r"C:\Users\gauta\PycharmProjects\OpenCV2\DataSets\mandril_color.tif"
        , img2 = r"C:\Users\gauta\PycharmProjects\OpenCV2\DataSets\mandril_color.tif"
        , img3 = r"C:\Users\gauta\PycharmProjects\OpenCV2\DataSets\cameraman.tif" )
