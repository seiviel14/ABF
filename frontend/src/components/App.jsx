import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Index } from './Index/Index';
import { Personaje } from "./Personajes/Personajes";

function App() {
    return (
        <div className='App'>
            <Routes>
                <Route path="/" element={<Index  />} />
                <Route path="/personaje/">
                    <Route path=":id" element={<Personaje />}/>
                </Route>
            </Routes>
        </div>
    );
}

export { App };