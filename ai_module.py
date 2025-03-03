from transformers import AutoModel, AutoTokenizer
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained('DiTy/bi-encoder-russian-msmarco')
model = AutoModel.from_pretrained('DiTy/bi-encoder-russian-msmarco')
model.to(device)


def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def embed_sentence(sentence):
    encoded_input = tokenizer(sentence, max_length=512, padding='max_length', truncation=True, return_tensors='pt')

    with torch.no_grad():
        model_output = model(**encoded_input)

    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

    return sentence_embeddings[0]


if __name__ == "__main__":
    sentences = [
        'красный плоский лишай вызван стрессом',
        'В большинстве случаев причину появления красного плоского лишая невозможно. Это не вызвано стрессом, но иногда эмоциональный стресс усугубляет ситуацию. Известно, что это заболевание возникает после контакта с определенными химическими веществами, такими как те, которые используются для проявления цветных фотографий. У некоторых людей определенные лекарства вызывают красный плоский лишай. Эти препараты включают лекарства от высокого кровяного давления, болезней сердца, диабета, артрита и малярии, антибиотики, нестероидные противовоспалительные обезболивающие и т. Д.',
        'К сожалению для работодателей, в разных штатах страны есть несколько дел, по которым суды установили, что стресс, вызванный работой, может быть основанием для увольнения с работы, если стресс достигает уровня серьезного состояния здоровья, которое вызывает они не могут выполнять свою работу.',
    ]

    for i in sentences:
        print(embed_sentence(i).shape)
