# image_comparator.py

import cv2

def compare_images(img_path1, img_path2):
    img1 = cv2.imread(img_path1)
    img2 = cv2.imread(img_path2)

    if img1 is None or img2 is None:
        print("[!] Ошибка загрузки изображений")
        return 0.0

    # Приводим к одному размеру
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Сравниваем по гистограммам
    hist1 = cv2.calcHist([gray1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])
    hist1 = cv2.normalize(hist1, hist1).flatten()
    hist2 = cv2.normalize(hist2, hist2).flatten()

    score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    print(f"[=] Оценка сходства: {score:.2f}")
    return score
