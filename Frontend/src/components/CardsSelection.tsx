"use client"

import React from "react";
import { Box, Card, CardActionArea, CardContent, Typography, useTheme } from "@mui/material";
import { useRouter } from "next/navigation";

export default function SelectionCards() {

    const appTheme = useTheme()
    const router = useRouter();
    
    const handleOnCreateButtonClick = () => {
        router.push("/configuration-items");
    };

    const handleOnReadButtonClick = () => {
        router.push("/read-items");
    };

  return (
    <Box
      sx={{
        display: "flex",
        gap: "64px",
        padding: "8px",
        width: "80%",
        boxSizing: "border-box",
      }}
    >
        <CardActionArea
            onClick={handleOnCreateButtonClick}
        >
            <Card
                sx={{
                    flex: 1,
                    borderRadius: 2,
                    padding: 2,
                    minHeight: 500,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    backgroundColor: appTheme.palette.primary.dark,
                    "&:hover": {
                        backgroundColor: appTheme.palette.secondary.dark,
                        color: appTheme.palette.getContrastText(appTheme.palette.secondary.dark),
                        transition: "background-color 0.3s ease",
                    }
                }}
            >
                
                    <CardContent>
                        <Typography variant="h5" align="center">
                            Generate Cisterciense Number
                        </Typography>
                    </CardContent>
                
            </Card>
        </CardActionArea>

        <CardActionArea
            onClick={handleOnReadButtonClick}
        >
            <Card
                sx={{
                flex: 1,
                borderRadius: 2,
                padding: 2,
                minHeight: 500,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                backgroundColor: appTheme.palette.primary.dark,
                "&:hover": {
                        backgroundColor: appTheme.palette.secondary.dark,
                        color: appTheme.palette.getContrastText(appTheme.palette.secondary.dark),
                        transition: "background-color 0.3s ease",
                    }
                }}
            >
                <CardContent>
                <Typography variant="h5" align="center">
                    Read Cisterciense Image
                </Typography>
                </CardContent>
            </Card>
        </CardActionArea>
    </Box>
  );
}
