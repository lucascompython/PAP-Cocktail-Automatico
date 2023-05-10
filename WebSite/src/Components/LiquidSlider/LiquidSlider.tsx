import { Slider, Checkbox, FormControlLabel } from "@mui/material";

import { useState } from "react";

const LiquidSlider = ({ sliders }) => {
    const [values, setValues] = useState(new Array(sliders.length).fill(0));
    const maxValue = 100;

    const [checked, setChecked] = useState(false);

    function handleChange(index: number, value: number) {
        const remaining = maxValue - value;
        setValues((vs) =>
            vs.map((v, i) => {
                if (i === index) return value;
                const oldRemaining = (maxValue - vs[index]) as number;
                if (!checked) return vs[i];

                if (oldRemaining) return (remaining * v) / oldRemaining;
                return remaining / (sliders.length - 1);
            })
        );
    }

    const handleCheckboxChange = (
        event: React.ChangeEvent<HTMLInputElement>
    ) => {
        setChecked(event.target.checked);

        if (event.target.checked) {
            const remaining = maxValue - values[0] - values[1] - values[2];
            const max = Math.max(...values);
            const sum = values.reduce((a, b) => a + b, 0);

            const maxCount = values.filter((v) => v === max).length;
            console.log(maxCount);

            if (maxCount === 3 && sum > maxValue) {
                setValues((vs) => vs.map((v) => v + remaining / 3));
                return;
            }

            setValues((vs) =>
                vs.map((v) => (v !== max ? v + remaining / (3 - maxCount) : v))
            );
        }
    };

    return (
        <>
            {sliders.map((item: string, index: number) => (
                <>
                    <p>Liquido Nº. {index + 1}</p>
                    <Slider
                        key={index}
                        value={values[index]}
                        title={item}
                        onChange={(_e, newNum) =>
                            handleChange(index, newNum as number)
                        }
                        valueLabelDisplay="auto"
                        valueLabelFormat={(v) => `${Math.round(v)}%`}
                        aria-label="slider"
                    />
                </>
            ))}
            <FormControlLabel
                label="Preencher"
                control={
                    <Checkbox
                        checked={checked}
                        onChange={handleCheckboxChange}
                        inputProps={{ "aria-label": "controlled" }}
                    />
                }
            />

            <p>
                Total:{" "}
                {values[0] + values[1] + values[2] < 100
                    ? Math.ceil(values[0] + values[1] + values[2])
                    : Math.floor(values[0] + values[1] + values[2])}
            </p>
        </>
    );
};

export default LiquidSlider;
