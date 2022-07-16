function List(props){
    function handleClick() {
        props.deletion(props.id)
    }

    return(
        <div className="personaje">
            <h1>Nombre: {props.nombre_personaje}</h1>
            <br />
            <button onClick={handleClick}>Eliminar</button>
        </div>
    )
}
export default List;