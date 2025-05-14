"use client"

import { PropsWithChildren } from "react";
import Navbar from "../../components/NavBar";
import { Box } from "@mui/material";

export default function NavBarLayout({children}: PropsWithChildren) {

    return (
        <>
            <Navbar />
            <Box sx={{ paddingTop: '68px' }} />
            {children}
        </>
    )
}