"use client"
import { Button, Paper, useTheme } from "@mui/material";
import TextField, { TextFieldRefProps } from "../../../components/Textfield";
import { useRef } from "react";

export default function ConfigurationItems() {

    const appTheme = useTheme()

    const textfieldNaturalNumberRef = useRef<TextFieldRefProps>(null);

    const generateCisterNumber = async () => {
        const naturalNumber = textfieldNaturalNumberRef.current?.getValue();
        alert(naturalNumber)
    }

    return (
        <Paper
            sx={{
                padding: 8,
                minHeight: 'calc(100vh - 68px)',
                boxSizing: 'border-box',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                backgroundColor: appTheme.palette.background.default,
            }}
        >
            <TextField
                ref={textfieldNaturalNumberRef}
                label="Natural Number"
                regularExpression={/^[0-9]{1,4}$/}
                sx={{
                    width: "80%",
                    margin: "16px"
                }}
            />
            <Button
                variant="contained"
                onClick={generateCisterNumber}
            >
                Submit Value
            </Button>
        </Paper>
    )
}