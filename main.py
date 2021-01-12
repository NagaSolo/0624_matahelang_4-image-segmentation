import pixellib
from pixellib.semantic import semantic_segmentation

segment_image = semantic_segmentation()
segment_image.load_pascalvoc_model("model/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
segment_image.segmentAsPascalvoc(
    "tests/bike_1000x-1.jpg", 
    output_image_name = "res/bike_1000_res",
    overlay=True)