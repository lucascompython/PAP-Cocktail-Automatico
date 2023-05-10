import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

import LiquidSlider from "./Components/LiquidSlider/LiquidSlider";

const App = () => {
    const [percentages, setPercentages] = useState([0, 0, 0]);
    const [error, setError] = useState(false);
    console.log(percentages);
    console.log(error);

    useEffect(() => {
        const get_percentages = async () => {
            const response = await fetch(
                "http://localhost:5000/get_percentages"
            );
            if (!response.ok) {
                setError(true);
                return;
            }
            const data = await response.json();
            setPercentages(data.percentages);
        };
        get_percentages();
    }, []);

    return (
        <>
            <h1>Cocktail Automático</h1>
            <div>
                <a href="https://vitejs.dev" target="_blank">
                    <img src={viteLogo} className="logo" alt="Vite logo" />
                </a>
                <a href="https://react.dev" target="_blank">
                    <img
                        src={reactLogo}
                        className="logo react"
                        alt="React logo"
                    />
                </a>
            </div>
            <div className="card">
                <p>Selecione a quantidade de cada liquido.</p>

                <LiquidSlider sliders={["slider 1", "slider 2", "slider 3"]} />
            </div>
            <p className="read-the-docs">
                Feito por Lucas Maciel de Linhares e Roberto Fernandes.
            </p>
        </>
    );
};

export default App;
