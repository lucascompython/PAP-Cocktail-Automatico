import { useState, useEffect } from "react";
import fotoModelo3D from "./assets/foto_modelo3d.webp";
import { Button } from "@mui/material";

import "./App.css";

import LiquidSlider from "./Components/LiquidSlider/LiquidSlider";

const start = async (liquido1: number, liquido2: number, liquido3: number) => {
    await fetch(
        `http://127.0.0.1:5000/start?liquido1=${liquido1}&liquido2=${liquido2}&liquido3=${liquido3}`,
        {
            method: "POST",
        }
    );
};

const App = () => {
    const [percentages, setPercentages] = useState([0, 0, 0]);
    const [error, setError] = useState(false);
    const [message, setMessage] = useState("");

    const sliders = ["slider 1", "slider 2", "slider 3"];

    const [values, setValues] = useState(new Array(sliders.length).fill(0));

    useEffect(() => {
        const get_percentages = async () => {
            const response = await fetch(
                "http://127.0.0.1:5000/get_percentages",
                {
                    method: "GET",
                }
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
            <h1>
                <a
                    href="https://github.com/lucascompython/PAP-Cocktail-Automatico"
                    target="_blank"
                >
                    Cocktail Automático
                </a>
            </h1>
            <div>
                <img
                    src={fotoModelo3D}
                    style={{ width: "70%", height: "70%" }}
                    alt="foto modelo 3d"
                />
            </div>
            <div className="card">
                <h2>Percentagens</h2>
                {message && <p>{message}</p>}

                {error ? (
                    <p>Erro ao carregar as percentagens</p>
                ) : (
                    <p>
                        {percentages[0]}% {percentages[1]}% {percentages[2]}%
                    </p>
                )}

                <p>Selecione a quantidade de cada liquido.</p>

                <LiquidSlider
                    sliders={sliders}
                    values={values}
                    setValues={setValues}
                />
            </div>
            <Button
                color="primary"
                variant="contained"
                onClick={() => {
                    const total = values.reduce((a, b) => a + b, 0);
                    if (total > 101) {
                        alert(
                            "A soma das percentagens não pode ser maior que 100%"
                        );
                        return;
                    }
                    start(values[0], values[1], values[2]);
                    setMessage("Cocktail iniciado");
                }}
            >
                Start
            </Button>
            <p className="read-the-docs">
                Feito por Lucas Maciel de Linhares e Roberto Fernandes.
            </p>
        </>
    );
};

export default App;
