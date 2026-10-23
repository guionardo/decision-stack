---
tipo: tecnologia
nome: Hono
categoria: Backend
url_oficial: https://hono.dev
urls_relacionadas:
  - https://hono.dev/docs/
  - https://github.com/honojs/hono
licenca: MIT
status: ativo
registrado: 2026-10-23
atualizado: 2026-10-23
tags: [catalogo, backend, web-framework, typescript, edge, serverless, api]
---

# Hono

> [!info] Documentação oficial
> https://hono.dev — docs em https://hono.dev/docs/ · repositório https://github.com/honojs/hono

## Resumo
Hono ("flame" em japonês) é um framework web pequeno, simples e ultra-rápido construído sobre Web Standards. O router RegExpRouter está entre os mais rápidos do ecossistema JavaScript e o preset `hono/tiny` tem menos de 14kB. O mesmo código roda em Cloudflare Workers, Fastly Compute, Deno, Bun, Vercel, Netlify, AWS Lambda, Lambda@Edge e Node.js.

## Problemas que resolve
- Escrever APIs/microserviços que precisam rodar em múltiplos runtimes (edge, serverless, Node) sem reescrever o código por plataforma.
- Bundle mínimo e cold start baixo — crítico em edge/serverless.
- Tipagem forte de rotas e validação com TypeScript first-class ("Now, we've got Types").
- Substituir frameworks pesados (Express-like) quando o alvo é performance e portabilidade.

## Objetivos / Quando usar
- APIs REST/RPC leves, microserviços, handlers de edge e servidores serverless.
- Quando se quer middleware built-in + de terceiros sem abrir mão de tamanho reduzido.
- Projetos novos onde portabilidade entre runtimes JS é requisito de decisão.

## Pontos de atenção
- Foco em HTTP/API — não é um framework full-stack com SSR de páginas no estilo Next/Nuxt (embora exista JSX e integrações).
- Ecossistema mais jovem que Express; menos middleware legado disponível.
- Zero dependências e MIT, sem custo de licença; custos ficam por conta do runtime (Workers, Lambda etc.).

## Alternativas
- Express / Fastify (Node tradicional, ecossistema maior, menos portáteis para edge)
- Elysia (Bun-first, tipagem agressiva)
- itty-router (Workers, ainda mais minimalista)
- (Nenhuma registrada no catálogo ainda — linkar quando catalogadas)

## Comentários
Bom fit com o stack TypeScript do usuário (Nuxt) para camadas de API edge/serverless; combina com deploy em Runpod serverless ou Cloudflare. Licença MIT sem restrições.

## Links
- [Documentação oficial](https://hono.dev/docs/)
- [Site](https://hono.dev)
- [GitHub](https://github.com/honojs/hono)

## Documentos relacionados
- [[_index]] — índice do catálogo
