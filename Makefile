.PHONY: help install html clean serve all

PYTHON := python3
PIP := pip3
OUTPUT_BASE := .
BUILD_DIR := $(OUTPUT_BASE)/_build

help:
	@echo "=== 파이토치 한국 사용자 모임 핸즈온 랩 빌드 도구 ==="
	@echo "make install  - 필요 패키지 설치"
	@echo "make html     - JupyterBook HTML 빌드"
	@echo "make clean    - 빌드된 파일 삭제"
	@echo "make serve    - 로컬 서버 실행 (http://localhost:8000)"
	@echo "make all      - 전체 과정 실행 (install + html + serve)"

install:
	$(PIP) install -r labs/requirements.txt
	@echo "✓ 패키지 설치 완료"

html: install
	jupyter-book build labs/ --path-output $(OUTPUT_BASE)
	@echo "✓ 빌드 완료: $(BUILD_DIR)/html/index.html"

clean:
	rm -rf $(BUILD_DIR)
	@echo "✓ 빌드 파일이 삭제되었습니다"

serve: html
	@echo "Starting server at http://localhost:8000"
	@cd $(BUILD_DIR)/html && $(PYTHON) -m http.server 8000

all: clean install html serve
