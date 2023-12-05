import React from 'react';
import {AppBar, Container, Toolbar, Typography} from "@mui/material";

const Header = () => {
    return (
        <AppBar position="static" className="appbar">
            <Container maxWidth="xl">
                <Toolbar disableGutters>
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
                        ANÁLISIS DE SENTIMIENTO
                    </Typography>
                </Toolbar>
            </Container>
        </AppBar>
    );
};

export default Header;