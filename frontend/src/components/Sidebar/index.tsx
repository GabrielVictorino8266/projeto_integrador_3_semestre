import { useState } from "react";
import Logo from "@assets/Logo.png";
import Sair from "@assets/Sair.png";
import User from "@assets/User.png";
import DashboardIcon from "@mui/icons-material/Dashboard";
import DirectionsBusIcon from "@mui/icons-material/DirectionsBus";
import BarChartIcon from "@mui/icons-material/BarChart";
import PersonIcon from "@mui/icons-material/Person";
import { useUsuario } from "@hooks/useUser/index";

import {
    Baseboard,
    Container,
    ItemContainer,
    Main,
    TitleContainer,
    UserContainer,
    Submenu,
    MenuItem,
    IconText,
    SubItem,
} from "./style";
import { useNavigate } from "react-router-dom";
import { logoutUser } from "@services/Api/LogoutUser";

export function Sidebar() {
    const [expanded, setExpanded] = useState<string | null>(null);
    const { user } = useUsuario();
    const navigate = useNavigate();

    const toggleExpand = (menu: string) => {
        setExpanded((prev) => (prev === menu ? null : menu));
    };

    return (
        <Container>
            <TitleContainer onClick={() => navigate("/dashboard")}>
                <img src={Logo} alt="Logo" />
                <p>
                    VIAÇÃO <br /> <span>UNIÃO</span>
                </p>
            </TitleContainer>

            <Main>
                <ItemContainer>
                    <ul>
                        <MenuItem onClick={() => toggleExpand("dashboard")}>
                            <IconText>
                                <DashboardIcon fontSize="small" />
                                DASHBOARD
                            </IconText>
                            <span>{expanded === "dashboard" ? "-" : "+"}</span>
                        </MenuItem>

                        <MenuItem onClick={() => toggleExpand("veiculos")}>
                            <IconText>
                                <DirectionsBusIcon fontSize="small" />
                                VEÍCULOS
                            </IconText>
                            <span>{expanded === "veiculos" ? "-" : "+"}</span>
                        </MenuItem>
                        {expanded === "veiculos" && (
                            <Submenu>
                                <SubItem>
                                    <a onClick={() => navigate("/veiculos")}>
                                        &gt; Cadastrar
                                    </a>
                                </SubItem>
                            </Submenu>
                        )}

                        <MenuItem onClick={() => toggleExpand("relatorios")}>
                            <IconText>
                                <BarChartIcon fontSize="small" />
                                RELATÓRIOS
                            </IconText>
                            <span>{expanded === "relatorios" ? "-" : "+"}</span>
                        </MenuItem>

                        {expanded === "relatorios" && (
                            <Submenu>
                                <SubItem>
                                    <a href="#">&gt; Cadastrar</a>
                                </SubItem>
                                <SubItem>
                                    <a href="#">&gt; Excluir</a>
                                </SubItem>
                            </Submenu>
                        )}

                        <MenuItem onClick={() => toggleExpand("usuarios")}>
                            <IconText>
                                <PersonIcon fontSize="small" />
                                USUÁRIOS
                            </IconText>
                            <span>{expanded === "usuarios" ? "-" : "+"}</span>
                        </MenuItem>

                        {expanded === "usuarios" && (
                            <Submenu>
                                <SubItem>
                                    <a onClick={() => navigate("/motorista")}>
                                        &gt; Cadastrar
                                    </a>
                                </SubItem>
                                <SubItem>
                                    <a href="#">&gt; Excluir</a>
                                </SubItem>
                            </Submenu>
                        )}
                    </ul>
                </ItemContainer>
            </Main>

            <Baseboard>
                <img src={User} alt="imagem-do-usuario" />
                <UserContainer>
                    <p>
                        <strong>{user ? user.nome : "Carregando..."}</strong>
                        <br />
                        <small>{user ? user.cargo : ""}</small>
                    </p>
                </UserContainer>
                <button
                    onClick={async () =>{
                        await logoutUser()
                        navigate("/login")
                    }}
                >
                    <img src={Sair} alt="Botão-sair" className="botao" />
                </button>
            </Baseboard>
        </Container>
    );
}
