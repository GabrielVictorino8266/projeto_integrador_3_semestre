import Logo from "@assets/IconeUniao.png";
import Sair from "@assets/Sair.png";
import User from "@assets/User.png";
import DashboardIcon from "@mui/icons-material/Dashboard";
import DirectionsBusIcon from "@mui/icons-material/DirectionsBus";
import PersonIcon from "@mui/icons-material/Person";
import { useUsuario } from "@hooks/useUser/index";

import {
    Baseboard,
    Container,
    ItemContainer,
    Main,
    TitleContainer,
    UserContainer,
    MenuItem,
    IconText,
} from "./style";
import { useNavigate } from "react-router-dom";
import { logoutUser } from "@services/Api/LogoutUser";

export function Sidebar() {
    const { user } = useUsuario();
    const navigate = useNavigate();

    return (
        <Container>
            <TitleContainer onClick={() => navigate("/dashboard/motoristas")}>
                <img src={Logo} alt="Logo" />
                <p>
                    VIAÇÃO <br /> <span>UNIÃO</span>
                </p>
            </TitleContainer>

            <Main>
                <ItemContainer>
                    <ul>
                        <MenuItem onClick={() => navigate("/dashboard/viagens")}>
                            <IconText>
                                <DashboardIcon fontSize="small" />
                                VIAGENS
                            </IconText>
                        </MenuItem>

                        <MenuItem onClick={() => navigate("/dashboard/veiculos")}>
                            <IconText onClick={() => navigate('dash')}>
                                <DirectionsBusIcon fontSize="small" />
                                VEÍCULOS 
                            </IconText>
                        </MenuItem>
                        <MenuItem onClick={() => navigate("/dashboard/motoristas")}>
                            <IconText>
                                <PersonIcon fontSize="small" />
                                USUÁRIOS
                            </IconText>
                        </MenuItem>
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
