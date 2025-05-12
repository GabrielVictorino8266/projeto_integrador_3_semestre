import styled from "@emotion/styled";
import VanFundo from '../../assets/VanFundo.png';
import Pessoa from '../../assets/Pessoa.png';
import Cadeado from '../../assets/Cadeado.png';

interface ImageProps {
    cadeado?: boolean;
}

export const Container = styled.div`
    display: flex;
    height: 100vh;
    width: 100%;
    margin: 0; 
    padding: 0; 
`;

export const LeftContainer = styled.div`
    width: 50%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #071425; 
    justify-content: center; 

    @media (max-width: 768px) {
        width: 100%;
        height: auto;  
        padding: 20px;
        justify-content: center; 
    }
`;

export const RightContainer = styled.div`
    width: 100%;
    height: 100vh;
    background-image: url(${VanFundo});
    background-position: center;
    background-size: cover;

    @media (max-width: 768px) {
        display: none; 
    }
`;

export const TitleDiv = styled.div`
    margin-top: 0;  
    display: flex;
    gap: 20px;
    align-items: flex-start;
    justify-content: center;

    img {
        height: 150px;

        @media (max-width: 768px) {
            height: 100px;
            display: none;
        }
    }

    h1 {
        font-size: 40px;
        color: #E0E0E0;
        span {
            font-size: 80px;
        }

        @media (max-width: 768px) {
            font-size: 28px;
            flex-direction: column;
        }
    }
`;

export const ContainerInput = styled.div<ImageProps>`
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: 100%;
    margin-bottom: 2%;

    label {
        font-size: 20px;
        color: #E0E0E0;
        font-weight: 400;

        @media (max-width: 768px) {
            font-size: 16px;
        }
    }

    input {
        background-image: url(${(props) => (props.cadeado ? Cadeado : Pessoa)});
        background-repeat: no-repeat;
        background-position: 10px center;
        background-size: 20px 20px;
        height: 49px;
        font-size: 20px;
        border-radius: 10px;
        color: black;
        padding-left: 40px;

        @media (max-width: 768px) {
            font-size: 16px;
        }
    }

    p {
        font-size: 14px;
        line-height: 80%;
        color: rgb(209, 100, 100);
    }
`;

export const Links = styled.div`
    display: flex;
    width: 100%;
    margin: 10px 0px;
    justify-content: space-between;

    a {
        color: #FF6F00;
        font-size: 14px;
    }

    @media (max-width: 768px) {
        flex-direction: column;
        gap: 8px;
        align-items: center;
    }
`;

export const BotaoEntrar = styled.button`
    background-color: #1189FF;
    border-radius: 10px;
    width: 410px;
    height: 70px;
    font-size: 24px;
    font-weight: 700;
    color: white;
    border: none;
    transition: all 0.3s ease;

    &:hover {
        background-color: rgb(53, 148, 243);
        transform: scale(1.05);
    }

    @media (max-width: 768px) {
        width: 100%;
        font-size: 20px;
        height: 60px;
    }
`;
