import styled from "@emotion/styled";
import pessoa from "@assets/Pessoa.png";
import cadeado from "@assets/Cadeado.png";
import lupa from "@assets/Lupa.png";

interface ImageProps {
    cadeado?: boolean;
    pessoa?: boolean;
    lupa?: boolean;
    error?: string;
    backgroundColor?: string;
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
    }

    input {
        width: 100%;
        height: 56px;
        border: none;
        border-radius: 32px;
        background: ${(p) => (p.error ? "var(--color-error-2)" : p.backgroundColor ?? "var(--color-input-background)")};
        background-image: ${(p) =>
            p.cadeado ? `url(${cadeado})` : p.pessoa ? `url(${pessoa})` : p.lupa ? `url(${lupa})` : "none"};
        background-repeat: no-repeat;
        background-position: 18px center;
        background-size: 24px 24px;
        padding-left: ${(p) => (p.cadeado || p.pessoa || p.lupa ? "60px" : "24px")};
        font-size: 20px;
        font-weight: 700;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
        outline: none;

        &::placeholder {
            font-style: italic;
            font-weight: 700;
            color: #7b7b7b;
        }
    }

    p {
        font-size: var(--font-size-12);
        color: var(--color-error);
        font-weight: 500;
        line-height: 80%;
    }
`;
