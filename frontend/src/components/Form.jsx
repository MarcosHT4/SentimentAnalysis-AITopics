import React, {useState} from 'react';
import {Button, Typography} from "@mui/material";
import api from "../api/text";

const Form = () => {
    const [message, setMessage] = useState("");
    const [sentimentResult, setSentimentResult] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            setIsLoading(true)
            const response = await api.post('/sentiment', message)
            setSentimentResult(response.data.score_output.label)
            setIsLoading(false)
        } catch (e) {
            console.error(e)
        }
    }
    return (
        <section>
            <form className="form" onSubmit={handleSubmit}>
                <div className="form__div">
                    <label>
                        <Typography
                            variant="h6"
                            noWrap
                            component="a"
                            sx={{
                                mr: 2,
                                display: { xs: 'none', md: 'flex' },
                                fontFamily: 'monospace',
                                fontWeight: 700,
                                letterSpacing: '.3rem',
                                color: 'inherit',
                                textDecoration: 'none',
                            }}
                        >
                            MENSAJE
                        </Typography>
                        <input type="text" value={message} onChange={(e) => {setMessage(e.target.value)}} />
                    </label>
                    <Button variant="contained" type="submit">
                        Submit
                    </Button>

                </div>

                {isLoading && (
                    <Typography
                        variant="h6"
                        noWrap
                        component="a"
                        sx={{
                            mr: 2,
                            display: { xs: 'none', md: 'flex' },
                            fontFamily: 'monospace',
                            fontWeight: 700,
                            letterSpacing: '.3rem',
                            color: 'inherit',
                            textDecoration: 'none',
                        }}
                    >
                        CARGANDO...
                    </Typography>
                )}


                {sentimentResult && (
                    <>
                        <Typography
                            variant="h6"
                            noWrap
                            component="a"
                            sx={{
                                mr: 2,
                                display: { xs: 'none', md: 'flex' },
                                fontFamily: 'monospace',
                                fontWeight: 700,
                                letterSpacing: '.3rem',
                                color: 'inherit',
                                textDecoration: 'none',
                            }}
                        >
                            EL MENSAJE PARA TU EX ES:
                        </Typography>
                        <Typography
                            variant="h6"
                            noWrap
                            component="a"
                            sx={{
                                mr: 2,
                                display: { xs: 'none', md: 'flex' },
                                fontFamily: 'monospace',
                                fontWeight: 700,
                                letterSpacing: '.3rem',
                                color: 'inherit',
                                textDecoration: 'none',
                            }}
                        >
                            {sentimentResult}
                        </Typography>
                    </>
                )}

            </form>
            
        </section>
    );
};

export default Form;