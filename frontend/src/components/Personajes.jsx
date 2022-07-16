import {useState, useEffect} from "react"
import axios from "axios"
import List from "./List"

function Personaje() {

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
            url: "/fichapersonaje/",
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
        }})
    }

    function crearPersonaje() {
        axios({
            method: "POST",
            url: "/fichapersonaje/",
            data: {
                nombre_personaje: formularioPersonaje.nombre_personaje
            }
        })
        .then((response) => {
            getPersonajes()
        })

        establecerFormularioPersonaje(({
            nombre_personaje: ""
        }))
        Event.preventDefault()
    }

    function deletePersonaje(id) {
        axios({
            method: "DELETE",
            url: `/fichapersonaje/${id}/`,
        })
        .then((response) => {
            getPersonajes()
        });
    }

    function handleChange(event) {
        const {value, name} = event.target
        establecerFormularioPersonaje(prevPersonaje =>({
            ...prevPersonaje, [name]: value
        })) 
    }

    return (
        <div className="">
            <form className="crear-personaje">
                <input onChange={handleChange} text={formularioPersonaje.nombre_personaje} name="nombre_personaje" placeholder="Nombre" value={formularioPersonaje.nombre_personaje}/>
                <br />
                <button onClick={crearPersonaje}>Crear personaje</button>
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
    )

}

export default Personaje;