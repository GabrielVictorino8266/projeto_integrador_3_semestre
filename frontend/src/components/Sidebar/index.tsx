import { useEffect, useState } from 'react';
import Logo from '../../assets/Logo.png';
import Sair from '../../assets/Sair.png';
import User from '../../assets/User.png';
import DashboardIcon from '@mui/icons-material/Dashboard';
import DirectionsBusIcon from '@mui/icons-material/DirectionsBus';
import BarChartIcon from '@mui/icons-material/BarChart';
import PersonIcon from '@mui/icons-material/Person';

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
  SubItem
} from './style';

type Usuario = {
  nome: string;
  cargo: string;
};

export function Sidebar() {
    const [expanded, setExpanded] = useState<string | null>(null);
    const [usuario, setUsuario] = useState<Usuario | null>(null);

    const toggleExpand = (menu: string) => {
        setExpanded(prev => (prev === menu ? null : menu));
    };

    useEffect(() => {
      const fetchUsuario = async () => {
          setTimeout(() => {
              const teste = {
                nome: 'Anderson',
                cargo: 'Administrador'
              };
              setUsuario(teste);
          }, 1000); 
      };
  
      fetchUsuario();
    }, []);

    return (
        <Container>
          <TitleContainer>
            <img src={Logo} alt="Logo" />
            <p>VIAÇÃO <br /> <span>UNIÃO</span></p>
          </TitleContainer>
    
          <Main>
              <ItemContainer>
                  <ul>
                    <MenuItem onClick={() => toggleExpand('dashboard')}>
                        <IconText>
                          <DashboardIcon fontSize="small" />
                          DASHBOARD
                        </IconText>
                        <span>{expanded === 'dashboard' ? '-' : '+'}</span>
                    </MenuItem>   
    
                    <MenuItem onClick={() => toggleExpand('veiculos')}>
                        <IconText>
                          <DirectionsBusIcon fontSize="small" />
                          VEÍCULOS
                        </IconText>
                        <span>{expanded === 'veiculos' ? '-' : '+'}</span>
                    </MenuItem> 
    
                    <MenuItem onClick={() => toggleExpand('relatorios')}>
                        <IconText>
                          <BarChartIcon fontSize="small" />
                          RELATÓRIOS
                        </IconText>
                        <span>{expanded === 'relatorios' ? '-' : '+'}</span>
                    </MenuItem>
                    
                    {expanded === 'relatorios' && (
                        <Submenu>
                            <SubItem><a href="#">&gt; Cadastrar</a></SubItem>
                            <SubItem><a href="#">&gt; Excluir</a></SubItem>
                        </Submenu>
                    )}    
    
                    <MenuItem onClick={() => toggleExpand('usuarios')}>
                        <IconText>
                            <PersonIcon fontSize="small" />
                            USUÁRIOS
                        </IconText>
                        <span>{expanded === 'usuarios' ? '-' : '+'}</span>
                    </MenuItem>
    
                    {expanded === 'usuarios' && (
                        <Submenu>
                            <SubItem><a href="#">&gt; Cadastrar</a></SubItem>
                            <SubItem><a href="#">&gt; Excluir</a></SubItem>
                        </Submenu>
                    )}
    
                  </ul>
              </ItemContainer>
          </Main>
    
          <Baseboard>
              <img src={User} alt="imagem-do-usuario" />
              <UserContainer>
                  <p>
                    <strong>{usuario ? usuario.nome : 'Carregando...'}</strong>
                    <br />
                    <small>{usuario ? usuario.cargo : ''}</small>
                  </p>
              </UserContainer>
              <button>
                  <img src={Sair} alt="Botão-sair" className='botao' />
              </button>
          </Baseboard>
        </Container>
    );
}
