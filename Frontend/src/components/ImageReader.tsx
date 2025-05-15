"use client"

import { Paper } from "@mui/material";
import { useEffect, useState } from "react";
import { generateCisterImage } from "../lib/requests/backendRequests";

type ImageReaderProps = {
  src: string;
  alt?: string;
  width?: number | string;
  height?: number | string;
};

export default function ImageReader({ src, alt = "", width = "100%", height = "auto" }: ImageReaderProps) {

    const [imageDefault, setImageDefault] = useState<string>();

    useEffect(() => {
        (async () => {
            const imageReturn = await generateCisterImage(3863);
            console.log("res",imageReturn)
            if (imageReturn.result) {
                console.log("type", typeof(imageReturn.result))
                setImageDefault(URL.createObjectURL(imageReturn.result))
            }
        })()
    })

    return (
        <Paper sx={{ padding: 2, display: 'flex', justifyContent: 'center', alignItems: 'center', width: "100%" }}>
            <img src={imageDefault} alt={alt} style={{ maxWidth: width, height: height }} />
        </Paper>
    );
}
