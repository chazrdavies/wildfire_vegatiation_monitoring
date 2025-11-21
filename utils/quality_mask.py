
# file for creating quality masks for Landsat images


def mask_from_bits(qa, bit):
    return (qa & (1 << bit)) > 0

def combined_mask(qa):
    cloud_mask       = mask_from_bits(qa, 5)
    shadow_mask      = mask_from_bits(qa, 3)
    snow_mask        = mask_from_bits(qa, 4)
    water_mask       = mask_from_bits(qa, 7)

    combined_mask = cloud_mask | shadow_mask | snow_mask | water_mask

    return combined_mask

def create_mask(arr):
    qa = arr[["qa_pixel"]].to_array().to_numpy()

    return combined_mask(qa)