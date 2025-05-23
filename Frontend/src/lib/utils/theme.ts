"use client"

import { createTheme } from "@mui/material";

const theme = createTheme({
    palette: {
        mode: "dark",
        primary: {
            main: "#c133ff",
            dark: "#8e00cc"
        },
        secondary: {
            main: "#b100ff",
            dark: "#4b006e",
        },
        background: {
            default: "#3a3a3a",
            paper: "#ffffff",
        },
    },
    shape: {
        borderRadius: 6,
    },
});

export default theme;