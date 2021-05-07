provider "google"{
    credentials = file("practica-312603-3aae22ea52d7.json")
    project = "practica-312603"
    region = "us-west1"
}


resource "google_compute_instance" "default"{}

##terraform import google_compute_instance.default practica-312603/us-west1-a/practica-312603--a9e77df795d7dda4