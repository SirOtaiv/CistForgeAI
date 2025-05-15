"use server"

import http from "http";
import https from "https";
import axios from "axios"
import { backendUrl } from "../utils/environmentVariables"
import RequestResponse from "../types/requestResponse"

export async function generateCisterImage(
    number: number,
) {
    let requestResponse: RequestResponse<Blob>

    try {
        const { data } = await axios.post(
            `${backendUrl}/image-generate/?number=${number}`,
            null,
            {
                httpAgent: new http.Agent({ keepAlive: true }),
                httpsAgent: new https.Agent({ keepAlive: true }),
                responseType: 'blob',
            },

        );

        console.log("",data.blob())

        requestResponse = {
            result: data.blob()
        }
    } catch (error: any) {
        requestResponse = {
            error: {
                message: "",
                status: error.status,
            },
        }
    }

    return requestResponse
}