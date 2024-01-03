al_service_image  := "pull_patrol_image"
al_service_container  := "pull_patrol_container"

default:
    just --list

build:
    docker build -t {{al_service_image}} .

cleanup:
    docker rm -f {{al_service_container}}

run:
    just cleanup
    docker run --name {{al_service_container}} -p 8000:8000 {{al_service_image}}

go:
    just build
    just run