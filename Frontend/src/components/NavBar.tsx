"use client"

import { AppBar, Toolbar, Tooltip, Icon, Typography, IconButton, styled, Box, useTheme } from "@mui/material";
import {
    AddCircleTwoTone as AddCircleTwoToneIcon,
    ImageSearch as ImageSearchIcon,
    HelpTwoTone as HelpTwoToneIcon,
    AccountCircleTwoTone as AccountCircleTwoToneIcon,
} from "@mui/icons-material";
import { useRouter } from "next/navigation";
import NoobsLink from "./NoobsLink";

const ImgIcon = styled("img")(() => ({
    height: "100%",
}));

const DivFlexGrow = styled("div")(() => ({
    flexGrow: 1,
}));


export default function Navbar() {

    const appTheme = useTheme();
    const router = useRouter();


    const handleOnCreateButtonClick = () => {
        router.push("/configuration-items");
    };

    const handleOnLogoIconClick = () => {
        router.push("/");
    };

    const getPersonPath = (): string => {
        return `/`;
    };


    return (<AppBar
                position="fixed"
                sx={{
                    zIndex: appTheme.zIndex.drawer + 1,
                    transition: appTheme.transitions.create(
                        ["width", "margin"],
                        {
                            easing: appTheme.transitions.easing.sharp,
                            duration:
                                appTheme.transitions.duration.leavingScreen,
                        },
                    ),
                    backgroundColor: "#4b006e"
                }}
            >

                <Toolbar>
                    <Tooltip title="Home">
                        <Box
                            sx={{
                                display: "flex",
                                alignItems: "center",
                                margin: "0 10px",
                            }}
                        >
                            <Icon
                                onClick={handleOnLogoIconClick}
                                sx={{
                                    fontSize: 68,
                                    display: "flex",
                                    textAlign: "center",
                                    cursor: "pointer",
                                }}
                            >
                                <ImgIcon alt="Noobs Corp" src="/NoobsCorp_Main_Icon.png" />
                            </Icon>
                            <Typography
                                noWrap
                                variant="h6"
                                sx={{
                                    cursor: "pointer",
                                    textDecoration: "none",
                                    color: "#fff",
                                }}
                            >
                                CISTIRCIAN PORTAL
                            </Typography>
                        </Box>
                    </Tooltip>
                    <DivFlexGrow />
                    <Tooltip
                        title={"NEW USER"}
                    >
                        <NoobsLink
                            href={getPersonPath()}
                        >
                            <Box
                                sx={{
                                    display: "flex",
                                    alignItems: "center",
                                    margin: "0 10px",
                                }}
                            >
                                <AccountCircleTwoToneIcon
                                    sx={{
                                        width: 40,
                                        height: 40,
                                        margin: "0 10px",
                                        display: "flex",
                                        color: "#fff",
                                    }}
                                />
                                <Typography
                                    noWrap
                                    variant="h6"
                                    sx={{
                                        color: "#fff",
                                        cursor: "pointer",
                                        textDecoration: "none",
                                        paddingRight: '8px',
                                    }}
                                    id="hello_page"
                                >
                                    NEW USER
                                </Typography>
                            </Box>
                        </NoobsLink>
                    </Tooltip>
                    <>
                        <Tooltip title="Generate Cisterciense Number">
                            <IconButton
                                id="new_item_header"
                                onClick={handleOnCreateButtonClick}
                            >
                                <AddCircleTwoToneIcon
                                    sx={{
                                        color: "#fff",
                                    }}
                                />
                            </IconButton>
                        </Tooltip>
                        <NoobsLink
                            href="/changelog/all"
                        >
                            <Tooltip title="Read Cisterciense Image">
                                <IconButton>
                                    <ImageSearchIcon
                                        sx={{
                                            color: "#fff",
                                        }}
                                    />
                                </IconButton>
                            </Tooltip>
                        </NoobsLink>
                    </>
                    <Tooltip title="Help">
                        <IconButton
                            color="inherit"
                            href={`https://github.com/SirOtaiv/CistForgeAI/blob/master/README.md`}
                            target="_blank"
                        >
                            <HelpTwoToneIcon />
                        </IconButton>
                    </Tooltip>
                </Toolbar>
            </AppBar>
    )
}