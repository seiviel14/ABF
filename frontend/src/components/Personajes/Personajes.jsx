import {useState, useEffect} from "react"
import axios from "axios"
import { List } from "../Lists/List"
import { useParams, Link, Navigate, useNavigate } from "react-router-dom"

function Personaje() {

    let navigate = useNavigate();
    let params = useParams();
    
    const [personaje, getData] = useState({
        id: params.id,
        nombre_personaje: ""
    })

    useEffect(() => {
        getPersonaje(personaje.id)
    },
    [])

    function getPersonaje(id) {
        axios({
            method: "GET",
            url: `/personaje/${id}`,
        }).then((response) => {
            const data = response.data
            getData(data)
        })
    }

    function deletePersonaje(id) {
        axios({
            method: "DELETE",
            url: `/personaje/${id}`
        })
        .then((response) => {
            navigate("/", {replace:true})
        });
    }

    return (
        <div className="">
            <button><Link to='/'>Volver al indice</Link></button>
            <br />
            <br />
            <List
                key={personaje.id}
                id={personaje.id}
                nombre_personaje={personaje.nombre_personaje}
                deletion={deletePersonaje}
            />
        </div>
    )
}

export { Personaje };