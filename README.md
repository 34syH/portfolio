# 이지한 포트폴리오

정보보안 분야를 공부하며 쌓은 경험과 기술을 소개하는 개인 포트폴리오입니다.
GitHub Pages에서 정적 사이트로 배포되며, Flask로도 로컬 미리보기가 가능합니다.

## 실행

```bash
uv sync
uv run flask --app app run --debug
```

브라우저에서 `http://127.0.0.1:5000`을 열면 됩니다. 또는 `index.html`을 직접 열어도 됩니다.

## 내용 수정

- `index.html`: 이름, 소개, 경력, 기술 스택, 링크
- `static/styles.css`: 색상, 여백, 글꼴, 반응형 디자인
- `static/script.js`: 등장 애니메이션과 현재 연도

기술 스택을 추가하려면 `skill-card` 블록의 항목과 설명을 수정하세요.
