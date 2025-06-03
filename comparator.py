from PIL import Image
from skimage.metrics import structural_similarity as ssim
import numpy as np

def compare_screenshots(path1, path2):
    img1 = np.array(Image.open(path1).convert('L'))  # в оттенках серого
    img2 = np.array(Image.open(path2).convert('L'))
    score, _ = ssim(img1, img2, full=True)
    return score
