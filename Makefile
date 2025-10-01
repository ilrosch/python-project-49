install:
	uv sync

build:
	uv build	

package-install:
	uv tool install dist/*.whl

package-install-force:
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl

brain-games:
	uv run brain-games