# utils.py

# 결과 필터링 함수
def filter_results(outputs, categories, threshold=0.5, klass=None):
  filtered_results = []

  for label, score, box in zip(outputs['labels'], outputs['scores'], outputs['boxes']):
    if score < threshold:
      continue

    if klass is not None and int(label) != klass:
      continue

    filtered_results.append({
      "class": int(label),
      "label": categories[int(label)],
      "score": float(score),
      "bbox": [float(coord) for coord in box]
    })

  return filtered_results


# 결과 필터링 함수 동작 확인
if __name__ == "__main__":
  sample_outputs = {
    "labels": [1, 1, 2, 3, 4],
    "scores": [0.9, 0.8, 0.7, 0.6, 0.5],
    "boxes": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
  }
  sample_categories = {1: "cat", 2: "dog", 3: "bird", 4: "fish"}

  print(filter_results(sample_outputs, sample_categories, 0.75))
