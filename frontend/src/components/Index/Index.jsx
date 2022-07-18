import { Personaje } from "../Personajes/Personajes"
import { List } from "../Lists/IndexList";
import { useState, useEffect, Children } from "react";
import axios from "axios";


function Index() {
    const [personajes, establecerNuevoPersonaje] = useState(null)
    const [formularioPersonaje, establecerFormularioPersonaje] = useState({
        nombre_personaje: "",
    })

    useEffect(() => {
        getPersonajes()
    },
    [])

    
    function getPersonajes() {
        axios({
            method: "GET",
            url: "/personaje/",
        })
        .then((response) => {
            const data = response.data
            establecerNuevoPersonaje(data)
        })
        .catch((error) => {
            if (error.response) {
                console.log(error.response);
                console.log(error.response.status);
                console.log(error.response.headers);
            }
        })
    }

    async function crearPersonaje() {
        await axios({
            method: "POST",
            url: "/personaje/",
            timeout: 200,
            data: {
                nombre_personaje: formularioPersonaje.nombre_personaje,
            },
            
        })
        .then((response) => {
            getPersonajes()
        })
        .catch((error) => {
            if (error.response) {
                console.log(error.response);
                console.log(error.response.status);
                console.log(error.response.headers);
            }
        });

        establecerFormularioPersonaje(({
            nombre_personaje: "",
        }))
    }

    function deletePersonaje(id) {
        axios({
            method: "DELETE",
            url: `/personaje/${id}`
        })
        .then((response) => {
            getPersonajes()
        });
    }

    function handleChange(event) {
        const {value, name} = event.target
        establecerFormularioPersonaje(prevPersonaje => ({
            ...prevPersonaje, [name]: value
        }))
    }

    
    return (
        <div className="">
            <form classname="crear-personaje">
                <input onChange={handleChange} text={formularioPersonaje.nombre_personaje} name="nombre_personaje" placeholder="nombre" value={formularioPersonaje.nombre_personaje} />
                <br />
                <button onClick={crearPersonaje}>Crear Personaje</button>
            </form>

            {
                personajes && personajes.map(personaje => <List
                key={personaje.id}
                id={personaje.id}
                nombre_personaje={personaje.nombre_personaje}
                deletion={deletePersonaje}
                />)
            }
        </div>

    );
}

export { Index };