import { Link, Outlet  } from "react-router-dom";

function List(props){
    function handleClick() {
        props.deletion(props.id)
    }

    return(
        <div className="indexPersonaje">
            <h1>Nombre: {props.nombre_personaje}</h1>
            <br />
            <button><Link to={`/personaje/${props.id}`} id={props.id} key={props.id}>Detalles</Link></button>    
            <br />
            <button onClick={handleClick}>Eliminar</button>
            <Outlet />
        </div>
    )
}
export { List };