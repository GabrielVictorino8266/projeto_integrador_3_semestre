import styled from "@emotion/styled";
import pessoa from "@assets/Pessoa.png";
import cadeado from "@assets/Cadeado.png";
import lupa from "@assets/Lupa.png";

interface ImageProps {
    cadeado?: boolean;
    pessoa?: boolean;
    lupa?: boolean;
    error?: string;
}

export const ContainerInput = styled.div<ImageProps>`
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: 100%;
    margin-bottom: 2%;

    label {
        font-size: 20px;
        font-weight: var(--font-weight-700);
        color: var(--color-white);

        @media (max-width: 768px) {
            font-size: 16px;
        }
    }

    input {
        width: 100%;
        box-sizing: border-box;
        background-image: ${(props) =>
            props.cadeado ? `url(${cadeado})` : props.pessoa ? `url(${pessoa})` : props.lupa ? `url(${lupa})` : "none"};
        background-repeat: no-repeat;
        background-position: 10px center;
        background-color: ${(props) => (props.error ? "var(--color-error-2)" : "var(--color-white)")};
        background-size: 20px 20px;
        height: 49px;
        font-size: 20px;
        border-radius: 10px;
        padding-left: ${(props) => (props.cadeado || props.pessoa || props.lupa ? "40px" : "10px")};

        @media (max-width: 768px) {
            font-size: 16px;
        }
    }

    p {
        font-size: var(--font-size-12);
        color: var(--color-error);
        font-weight: 500;
        line-height: 80%;
    }
`;
