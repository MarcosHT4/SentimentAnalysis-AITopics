import React from 'react';
import {Typography} from "@mui/material";

const Description = () => {
    return (
        <section className="description">
            <Typography
                variant="h5"
                component="a"
                sx={{
                    mr: 2,
                    display: { xs: 'none', md: 'flex' },
                    fontFamily: 'monospace',
                    fontWeight: 700,
                    letterSpacing: '.3rem',
                    color: 'inherit',
                    textDecoration: 'none',
                    textAlign: 'center',
                }}
            >
                ¿Quieres recuperar a tu ex, pero no sabes cómo?
                ¡No te preocupes! Con nuestro análisis de sentimiento,
                podrás saber si el mensaje que le quieres enviar es el correcto.
            </Typography>
            <Typography
                variant="h6"
                component="a"
                sx={{
                    mr: 2,
                    display: { xs: 'none', md: 'flex' },
                    fontFamily: 'monospace',
                    fontWeight: 700,
                    letterSpacing: '.3rem',
                    color: 'inherit',
                    textDecoration: 'none',
                    textAlign: 'center',
                }}
            >
                Nuestra API, analizará el mensaje que le quieres enviar a tu ex, y te dirá si es el correcto.
            </Typography>


        </section>
    );
};

export default Description;