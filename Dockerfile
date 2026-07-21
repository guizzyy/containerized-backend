FROM python:3.14-alpine AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip -m install --no-cache-dir requirements.txt

FROM scratch

COPY --from=builder /app .

EXPOSE 8000

# CMD ["fastapi", "dev"]