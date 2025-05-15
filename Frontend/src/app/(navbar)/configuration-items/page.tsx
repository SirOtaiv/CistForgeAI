"use client"
import { Box, Button, Paper, useTheme } from "@mui/material";
import TextField, { TextFieldRefProps } from "../../../components/Textfield";
import { useRef } from "react";
import ImageReader from "../../../components/ImageReader";

export default function ConfigurationItemsPage() {

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
                flexDirection: 'column',
                gap: 4,
            }}
        >
            <Box
                sx={{
                    width: "100%",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    gap: 2,
                    flexDirection: "row",
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
            </Box>
            <Box
                sx={{
                    width: "100%",
                    display: "flex",
                    justifyContent: "center",
                }}
            >
                <ImageReader src="/next.svg" alt="Number" />
            </Box>
        </Paper>
    )
}