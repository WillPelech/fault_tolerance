FROM golang:1.22

WORKDIR /app
COPY go.mod go.sum ./

# If you have local replaces, copy those folders too before download:
COPY shared/ ./shared/
# (add any other local modules referenced by replace)

RUN go mod download
COPY . .

RUN go build -o app ./cmd/node

CMD ["./app"]
