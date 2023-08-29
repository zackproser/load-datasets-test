import pinecone
from pinecone_datasets import load_dataset


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':

    pinecone.init(api_key="<your-api-key>",
                  environment="us-west4-gcp-free")

    # indices = pinecone.list_indexes()
    dataset = load_dataset("quora_all-MiniLM-L6-bm25")
    for batch in dataset.iter_documents(batch_size=100):
        print("wakka")
        # index.upsert(vectors=batch)

    print_hi('test')
