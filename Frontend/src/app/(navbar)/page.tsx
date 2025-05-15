"use client"
import { Paper, useTheme } from "@mui/material";
import SelectionCards from "../../components/CardsSelection";

export default function Home() {

  const appTheme = useTheme();

  return (
      <Paper
        sx={{
          padding: 2,
          minHeight: 'calc(100vh - 68px)',
          boxSizing: 'border-box',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: appTheme.palette.background.default,
        }}
      >
        <SelectionCards />
      </Paper>
  );
}
