def setup(subparsers):
    classify = subparsers.add_parser(
        "classify",
        help="Classify proteins using either pretrained classifiers or train/test your own.")

    classify.add_argument(
        "classifier",
        help="Predict thermostability/optimal enzymatic pH using TemStaPro/EpHod or choose custom to train/use your "
             "own XGBoost, Multilayer perceptron, LightGBM or Isolation Forest classifier. ESM2+MLP allows you to train an ESM2 model with a classification head end-to-end.",
        choices=("TemStaPro", "EpHod", "M-Ionic", "ECPICK", "PSALM", "CatPred", "CataPro", "PSICHIC", "MLP", "XGBoost", "LightGBM", "iForest", "ESM2+MLP")
    )
    classify.add_argument(
        "query",
        help="Fasta file of sequences to score",
        action="store"
    )
    classify.add_argument(
        "--key",
        help="Input a CSV, with your class mappings for your embeddings where the first column is the label and the "
             "second column is the class.",
        action="store"
    )
    classify.add_argument(
        "--smiles",
        help="CatPred/CataPro: Input a plain text file with the ending .smiles that has a SMILES for inhibitor/substrate or a concatenated SMILES string for reactions with reactants separated by '.' Note that for CataPro, it only returns kcat and km, don't provide any multiple smiles with periods.",
        action="store"
    )
    classify.add_argument(
        "--save_emb",
        help="Save csv of embeddings",
        action="store_true",
        default=False
    )
    classify.add_argument(
        "--emb_model",
        help="Select desired protein language model for embedding your query proteins to then train your custom "
             "classifier. Default is esm2_t12_35M",
        default="esm2_t12_35M",
        action="store",
        choices= ("Ankh", "Ankh-Large", "CaLM", "esm2_t6_8M", "esm2_t12_35M", "esm2_t30_150M", "esm2_t33_650M", "esm2_t36_3B", "esm2_t48_15B",
                 "ProtT5-XL", "ProstT5", "RiNALMo", "mRNA-FM", "RNA-FM", "SaProt")
    )
    classify.add_argument(
        "--train_split",
        help="Choose your train-test percentage split for training and evaluating your custom classifier. For "
             "example, --train .6 would split your input sequences into two groups, one with 60%% of the sequences to "
             "train and the other with 40%% for evaluating",
        action="store",
    )
    classify.add_argument(
        "--preTrained",
        help="Enter the path to your pre-trained classifier that you've trained with TRILL. This will "
             "be a .json file.",
        action="store",
    )

    classify.add_argument(
        "--preComputed_Embs",
        help="Enter the path to your pre-computed embeddings. Make sure they match the --emb_model you select.",
        action="store",
        default=False
    )

    classify.add_argument(
        "--batch_size_emb",
        help="EpHod: Sets batch_size for embedding with ESM1v.",
        action="store",
        default=1
    )

    classify.add_argument(
        "--batch_size_mlp",
        help="MLP: Sets batch_size for training/evaluating",
        action="store",
        default=1
    )

    classify.add_argument(
        "--xg_gamma",
        help="XGBoost: sets gamma for XGBoost, which is a hyperparameter that sets 'Minimum loss reduction required "
             "to make a further partition on a leaf node of the tree.'",
        action="store",
        default=0.4
    )

    classify.add_argument(
        "--lr",
        help="XGBoost/LightGBM/ESM2+MLP/MLP: Sets the learning rate. Default is 0.0001 for ESM2+MLP/MLP, 0.2 for XGBoost and LightGBM",
        action="store",
        default=0.2
    )

    classify.add_argument(
        "--max_depth",
        help="XGBoost/LightGBM: Sets the maximum tree depth",
        action="store",
        default=8
    )

    classify.add_argument(
        "--num_leaves",
        help="LightGBM: Sets the max number of leaves in one tree. Default is 31",
        action="store",
        default=31
    )

    classify.add_argument(
        "--bagging_freq",
        help="LightGBM: Int that allows for bagging, which enables random sampling of training data of traingin data. For example, if it is set to 3, LightGBM will randomly sample the --bagging_frac of the data every 3rd iteration. Default is 0",
        action="store",
        default=0
    )

    classify.add_argument(
        "--bagging_frac",
        help="LightGBM: Sets fraction of training data to be used when bagging. Must be 0 < --bagging_frac <= 1. Default is 1",
        action="store",
        default=1
    )

    classify.add_argument(
        "--feature_frac",
        help="LightGBM: Sets fraction of training features to be randomly sampled for use in training. Must be 0 < --feature_frac <= 1. Default is 1",
        action="store",
        default=1
    )

    classify.add_argument(
        "--xg_reg_alpha",
        help="XGBoost: L1 regularization term on weights",
        action="store",
        default=0.8
    )

    classify.add_argument(
        "--xg_reg_lambda",
        help="XGBoost: L2 regularization term on weights",
        action="store",
        default=0.1
    )
    classify.add_argument(
        "--if_contamination",
        help="iForest: The amount of outliers in the data. Default is automatically determined, but you can set it "
             "between (0 , 0.5])",
        action="store",
        default="auto"
    )
    classify.add_argument(
        "--n_estimators",
        help="XGBoost/LightGBM: Number of boosting rounds",
        action="store",
        default=115
    )
    classify.add_argument(
        "--sweep",
        help="XGBoost/LightGBM: Use this flag to perform optimization over the hyperparameter space.",
        action="store_true",
        default=False
    )
    # classify.add_argument(
    #     "--sweep_cv",
    #     help="XGBoost/LightGBM: Change the number of folds used for cross-validation.",
    #     action="store",
    #     default=3
    # )
    classify.add_argument(
        "--sweep_iters",
        help="XGBoost/LightGBM: Change the number of optimization iterations. Default is 10.",
        action="store",
        default=10
    )
    classify.add_argument(
        "--f1_avg_method",
        help="XGBoost/LightGBM: Change the scoring method used for calculated F1. Default is with no averaging.",
        action="store",
        default=None,
        choices=("macro", "weighted", "micro", "None")
    )

    classify.add_argument(
        "--epochs",
        help="ESM2+MLP/MLP: Set number of epochs to train ESM2+MLP classifier.",
        action="store",
        default=3
    )

    classify.add_argument(
        "--hidden_layers",
        help="MLP: Set number of hidden layers. Default is [128,64,32]",
        action="store",
        default=[128,64,32]
    )

    classify.add_argument(
        "--dropout",
        help="MLP: Set dropout rate. Default is 0.3",
        action="store",
        default=0.3
    )

    classify.add_argument(
        "--db",
        help="3Di-Search: Specify the path of the fasta file for your database that you want to query against.",
        action="store",
    )

    classify.add_argument(
        "--poolparti",
        help="ESM2: Use Pool PaRTI based embeddings for training and evaluating classifier.",
        action="store_true",
        default=False
    )

def run(args):
    import builtins
    import logging
    import os
    import shutil
    import subprocess
    import sys

    import esm
    import numpy as np
    import pandas as pd
    import re
    import pytorch_lightning as pl
    import skops.io as sio
    import torch
    import xgboost as xgb
    from Bio import SeqIO
    from git import Repo
    from sklearn.ensemble import IsolationForest
    from sklearn.preprocessing import LabelEncoder
    from tqdm import tqdm
    from loguru import logger 
    from icecream import ic
    from sklearn.metrics import precision_recall_fscore_support
    import trill.utils.ephod_utils as eu
    import pkg_resources
    from trill.utils.safe_load import safe_torch_load
    from trill.commands.fold import process_sublist
    from trill.utils.MLP import MLP_C2H2, inference_epoch
    from trill.utils.classify_utils import prep_data, setup_esm2_hf, prep_foldseek_dbs, get_3di_embeddings, log_results, sweep, prep_hf_data, custom_esm2mlp_test, train_model, load_model, custom_model_test, predict_and_evaluate
    from trill.utils.esm_utils import parse_and_save_all_predictions, convert_outputs_to_pdb
    from trill.utils.lightning_models import ProtT5, CustomWriter, ProstT5, MLP_Classifier, MLP_Emb_Dataset_train, MLP_Emb_Dataset_test
    from unittest.mock import patch
    from ecpick import ECPICK
    import torch.nn.functional as F
    from torch.utils.data import DataLoader, Dataset
    from trill.utils.dock_utils import downgrade_biopython, upgrade_biopython, get_current_biopython_version
    from trill.utils.mionic_utils import mionic, IonicProtein, download_mionic_checkpoint
    from trill.utils.catpred import clone_and_install_catpred, download_catpred_weights, tupulize_fasta_smiles, create_csv_sh, get_rotary_emb_version, upgrade_rotary_emb, downgrade_rotary_emb, get_predictions
    from trill.utils.catapro import clone_and_install_catapro, fetch_molt5, fetch_prott5, run_catapro_prediction
    import trill.utils.catapro
    from trill.utils.psichic import clone_and_install_psichic, fasta_smiles_to_dataframe, run_psichic
    import matplotlib.pyplot as plt
    from urllib.request import urlretrieve

   
    from .commands_common import cache_dir, get_logger

    ml_logger = get_logger(args)

    def noop(*args, **kwargs):
        pass
            
    class CustomDataset(torch.utils.data.Dataset):
        def __init__(self, data):
            self.data = data

        def __len__(self):
            return len(self.data)

        def __getitem__(self, idx):
            return self.data[idx]

    if args.sweep and not args.train_split:
        logger.error("You need to provide a train-test fraction with --train_split!")
        raise Exception("You need to provide a train-test fraction with --train_split!")

    if args.classifier == 'M-Ionic':
        mionic_path = download_mionic_checkpoint(cache_dir)
        if not args.preComputed_Embs:
            embed_command = (
                "trill",
                args.name,
                args.GPUs,
                "--outdir", args.outdir,
                "embed",
                "esm2_t33_650M",
                args.query,
                "--per_AA"
            )
            logger.info("Extracting embeddings from ESM2-650M...")
            subprocess.run(embed_command, check=True)
            perAA = safe_torch_load(os.path.join(args.outdir, f"{args.name}_esm2_t33_650M_perAA.pt"), weights_only=False)
        else:
            perAA = safe_torch_load(args.preComputed_Embs, weights_only=False)

        model = IonicProtein(1280)
        preds, peraa_preds = mionic(args, perAA, model, mionic_path)
        mionic_preds = pd.DataFrame.from_dict(preds, orient='index').reset_index()
        mionic_preds.rename(columns={'index': 'Label'}, inplace=True)
        mionic_preds.to_csv(os.path.join(args.outdir, f"{args.name}_M-Ionic_preds.csv"), index=False)

        max_residues = max(len(residues) for residues in peraa_preds.values())

        rows = []

        for seq_id, residue_preds in peraa_preds.items():
            row = {'Label': seq_id}
            
            for i in range(max_residues):
                if i < len(residue_preds):
                    preds = residue_preds[i]
                    ion_preds = ' '.join(f"{ion}:{int(val)}" for ion, val in preds.items())
                else:
                    ion_preds = "NA"
                row[f"res{i+1}"] = ion_preds
            
            rows.append(row)

        peraa_preds_df = pd.DataFrame(rows)
        peraa_preds_df.to_csv(os.path.join(args.outdir, f"{args.name}_M-Ionic_perAA_preds.csv"), index=False)

    if args.classifier == 'CataPro':
        if not args.smiles:
            logger.error("You need to provide a .smiles file for predicting kinetics with CataPro")
            raise Exception("You need to provide a .smiles file for predicting kinetics with CataPro")
        clone_and_install_catapro(cache_dir)
        molt5_loc = fetch_molt5()
        prott5_loc = fetch_prott5()
        catapro_input_df = trill.utils.catapro.fasta_smiles_to_dataframe(args.query, args.smiles)
        catapro_input_df.to_csv(f'{args.name}_CataPro_input.csv')
        run_catapro_prediction(args, cache_dir)


    if args.classifier == 'PSICHIC':
        if not args.smiles:
            logger.error("You need to provide a .smiles file for predicting interactions with PSICHIC")
            raise Exception("You need to provide a .smiles file for predicting interactions with PSICHIC")
        clone_and_install_psichic(cache_dir)
        psichic_input_df = fasta_smiles_to_dataframe(args.query, args.smiles)
        psichic_input_df.to_csv(f'{args.name}_PSICHIC_input.csv')
        args.input_csv = f'{args.name}_PSICHIC_input.csv'
        # Set up path to cache_dir/PSICHIC
        psichic_path = os.path.join(cache_dir, "PSICHIC")
        sys.path.insert(0, psichic_path)
        run_psichic(args, cache_dir)

    if args.classifier == 'CatPred':
        preds_4_export = []

        if not args.smiles:
            logger.error("You need to provide a .smiles file for predicting kinetics with CatPred")
            raise Exception("You need to provide a .smiles file for predicting kinetics with CatPred")

        clone_and_install_catpred(cache_dir)
        download_catpred_weights(cache_dir)

        if not (args.smiles.endswith(".smiles") or args.smiles.endswith(".SMILES")):
            raise ValueError("Input file must end with .smiles or .SMILES")

        og_ver_rotary = get_rotary_emb_version()
        downgrade_rotary_emb()

        pairs_list = tupulize_fasta_smiles(args)
        args.cache_dir = cache_dir
        preds_4_export_ki = []
        preds_4_export_km = []

        for seq_name, seq_seq, smiles_name, smiles_smiles in pairs_list:
            if smiles_smiles.count('.') >= 1:
                _, _, sh_path = create_csv_sh('kcat', seq_name, seq_seq, smiles_smiles, smiles_name, args)
                flag = int(int(args.GPUs) == 0)
                command = (
                    f"export PROTEIN_EMBED_USE_CPU={flag} && "
                    f"chmod +x {os.path.join(args.outdir, sh_path)} && "
                    f"bash {os.path.join(args.outdir, sh_path)}"
                )
                status = subprocess.call(command, shell=True, executable="/bin/bash", stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                if status == 0:
                    logger.success('Prediction successful!\n')
                    unc, epi_unc, alea_unc, prediction, prediction_linear = get_predictions('kcat', seq_name)
                    preds_4_export.append((seq_name, smiles_name, unc, epi_unc, alea_unc, prediction_linear, seq_seq, smiles_smiles))
                    logger.success(f'kcat Prediction = {prediction_linear} mM')
                    logger.success(f'kcat Total Uncertainty = {unc}\n')
                else:
                    logger.error('Prediction failed!\n')

                catpred_df = pd.DataFrame(
                    preds_4_export,
                    columns=[
                        'Protein_Name',
                        'SMILES_Name',
                        'Total_Uncertainty',
                        'Epistemic_Uncertainty',
                        'Aleatoric_Uncertainty',
                        'kcat_s^{-1}',
                        'Protein_Sequence',
                        'SMILES_String'
                    ]
                )
                catpred_df.to_csv(os.path.join(args.outdir, f'{args.name}_kcat_catpred_results.csv'), index=False)

            else:
                for param in ['ki', 'km']:
                    _, _, sh_path = create_csv_sh(param, seq_name, seq_seq, smiles_smiles, smiles_name, args)
                    flag = int(int(args.GPUs) == 0)
                    command = (
                        f"export PROTEIN_EMBED_USE_CPU={flag} && "
                        f"chmod +x {os.path.join(args.outdir, sh_path)} && "
                        f"bash {os.path.join(args.outdir, sh_path)}"
                    )
                    status = subprocess.call(command, shell=True, executable="/bin/bash", stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                    if status == 0:
                        logger.success('Prediction successful!')
                        unc, epi_unc, alea_unc, prediction, prediction_linear = get_predictions(param, seq_name)
                        record = (seq_name, smiles_name, unc, epi_unc, alea_unc, prediction_linear, seq_seq, smiles_smiles)
                        if param == 'ki':
                            preds_4_export_ki.append(record)
                        elif param == 'km':
                            preds_4_export_km.append(record)
                        logger.success(f'{param} Prediction = {prediction_linear} mM')
                        logger.success(f'{param} Total Uncertainty = {unc}\n')

                    else:
                        logger.error('Prediction failed!\n')

        # Export ki predictions
        if preds_4_export_ki:
            df_ki = pd.DataFrame(
                preds_4_export_ki,
                columns=[
                    'Protein_Name',
                    'SMILES_Name',
                    'ki_Total_Uncertainty',
                    'ki_Epistemic_Uncertainty',
                    'ki_Aleatoric_Uncertainty',
                    'ki_mM',
                    'Protein_Sequence',
                    'SMILES_String'
                ]
            )
            df_ki.to_csv(os.path.join(args.outdir, f'{args.name}_ki_catpred_results.csv'), index=False)

        # Export k predictions
        if preds_4_export_km:
            df_km = pd.DataFrame(
                preds_4_export_km,
                columns=[
                    'Protein_Name',
                    'SMILES_Name',
                    'km_Total_Uncertainty',
                    'km_Epistemic_Uncertainty',
                    'km_Aleatoric_Uncertainty',
                    'km_mM',
                    'Protein_Sequence',
                    'SMILES_String'
                ]
            )
            df_km.to_csv(os.path.join(args.outdir, f'{args.name}_km_catpred_results.csv'), index=False)

            
        upgrade_rotary_emb(og_ver_rotary)
        # with open(args.smiles, 'r') as f:
        #     content = f.read()
        # rxn_counts = content.count('.')
    
        

    if args.classifier == 'ECPICK':
        args.cache_dir = cache_dir
        ecpick = ECPICK(args)
        ecpick.predict_fasta(fasta_path=args.query, output_path=args.outdir, args=args)

    # if args.classifier == "TemStaPro":
        # if not args.preComputed_Embs:
        #     data = esm.data.FastaBatchedDataset.from_file(args.query)
        #     model = ProtT5(args)
        #     pred_writer = CustomWriter(output_dir=args.outdir, write_interval="epoch")
        #     dataloader = torch.utils.data.DataLoader(data, shuffle=False, batch_size=1, num_workers=0)
        #     if int(args.GPUs) > 0:
        #         trainer = pl.Trainer(enable_checkpointing=False, callbacks=[pred_writer], devices=int(args.GPUs), accelerator="gpu",
        #                              logger=ml_logger, num_nodes=int(args.nodes))
        #     else:
        #         trainer = pl.Trainer(enable_checkpointing=False, callbacks=[pred_writer], logger=ml_logger, num_nodes=int(args.nodes))
        #     reps = trainer.predict(model, dataloader)
        #     parse_and_save_all_predictions(args)
        # if not os.path.exists(os.path.join(cache_dir, "TemStaPro_models")):
        #     temstapro_models = Repo.clone_from("https://github.com/martinez-zacharya/TemStaPro_models",
        #                                        os.path.join(cache_dir, "TemStaPro_models"))
        #     temstapro_models_root = temstapro_models.git.rev_parse("--show-toplevel")
        # else:
        #     temstapro_models = Repo(os.path.join(cache_dir, "TemStaPro_models"))
        #     temstapro_models_root = temstapro_models.git.rev_parse("--show-toplevel")
        # THRESHOLDS = ("40", "45", "50", "55", "60", "65")
        # SEEDS = ("41", "42", "43", "44", "45")
        # if not args.preComputed_Embs:
        #     emb_df = pd.read_csv(os.path.join(args.outdir, f"{args.name}_ProtT5_AVG.csv"))
        # else:
        #     emb_df = pd.read_csv(args.preComputed_Embs)
        # embs = emb_df[emb_df.columns[:-1]].applymap(lambda x: torch.tensor(x)).values.tolist()
        # labels = emb_df.iloc[:, -1]
        # list_of_tensors = [torch.tensor(l) for l in embs]
        # input_data = list(zip(list_of_tensors, labels))
        # custom_dataset = CustomDataset(input_data)
        # emb_loader = torch.utils.data.DataLoader(custom_dataset, shuffle=False, batch_size=1, num_workers=0)
        # inferences = {}
        # for thresh in THRESHOLDS:
        #     threshold_inferences = {}
        #     for seed in SEEDS:
        #         clf = MLP_C2H2(1024, 512, 256)
        #         clf.load_state_dict(torch.load(os.path.join(
        #             temstapro_models_root, f"mean_major_imbal-{thresh}_s{seed}.pt")))
        #         clf.eval()
        #         if int(args.GPUs) > 0:
        #             clf.to("cuda")
        #             threshold_inferences[seed] = inference_epoch(clf, emb_loader, device="cuda")
        #         else:
        #             threshold_inferences[seed] = inference_epoch(clf, emb_loader, device="cpu")
        #     for seq in threshold_inferences["41"].keys():
        #         mean_prediction = 0
        #         for seed in SEEDS:
        #             mean_prediction += threshold_inferences[seed][seq]
        #         mean_prediction /= len(SEEDS)
        #         binary_pred = builtins.round(mean_prediction)
        #         inferences[f"{seq}$%#{thresh}"] = (mean_prediction, binary_pred)
        # inference_df = pd.DataFrame.from_dict(inferences, orient="index", columns=("Mean_Pred", "Binary_Pred"))
        # inference_df = inference_df.reset_index(names="RawLab")
        # inference_df["Protein"] = inference_df["RawLab"].apply(lambda x: x.split("$%#")[0])
        # inference_df["Threshold"] = inference_df["RawLab"].apply(lambda x: x.split("$%#")[-1])
        # inference_df = inference_df.drop(columns="RawLab")
        # inference_df = inference_df[["Protein", "Threshold", "Mean_Pred", "Binary_Pred"]]
        # inference_df.to_csv(os.path.join(args.outdir, f"{args.name}_TemStaPro_preds.csv"), index=False)
        # if not args.save_emb and not args.preComputed_Embs:
        #     os.remove(os.path.join(args.outdir, f"{args.name}_ProtT5_AVG.csv"))


    if args.classifier == "TemStaPro":
        if not args.preComputed_Embs:
            data = esm.data.FastaBatchedDataset.from_file(args.query)
            model = ProtT5(args)
            pred_writer = CustomWriter(output_dir=args.outdir, write_interval="epoch")
            dataloader = DataLoader(data, shuffle=False, batch_size=1, num_workers=0)
            trainer = pl.Trainer(
                enable_checkpointing=False,
                callbacks=[pred_writer],
                devices=int(args.GPUs) if int(args.GPUs) > 0 else None,
                accelerator="gpu" if int(args.GPUs) > 0 else None,
                logger=ml_logger,
                num_nodes=int(args.nodes),
            )
            reps = trainer.predict(model, dataloader)
            parse_and_save_all_predictions(args)

        model_dir = os.path.join(cache_dir, "TemStaPro_new_models")
        os.makedirs(model_dir, exist_ok=True)
        
        THRESHOLDS = ("40", "45", "50", "55", "60", "65", "70", "75", "80")
        SEEDS = ("1", "2", "3", "4", "5")
        
        def download_model(thresh, seed):
            model_name = f"mean_major_imbal-{thresh}_s{seed}.pt"
            model_path = os.path.join(model_dir, model_name)
            model_url = f"https://github.com/ievapudz/TemStaPro/raw/main/models/{model_name}"
            if not os.path.exists(model_path):
                print(f"Downloading {model_name}...")
                urlretrieve(model_url, model_path)
            return model_path

        if not args.preComputed_Embs:
            emb_df = pd.read_csv(os.path.join(args.outdir, f"{args.name}_ProtT5_AVG.csv"))
        else:
            emb_df = pd.read_csv(args.preComputed_Embs)

        embs = emb_df.iloc[:, :-1].applymap(lambda x: torch.tensor(x)).values.tolist()
        labels = emb_df.iloc[:, -1]
        list_of_tensors = [torch.tensor(l) for l in embs]
        input_data = list(zip(list_of_tensors, labels))
        custom_dataset = CustomDataset(input_data)
        emb_loader = DataLoader(custom_dataset, shuffle=False, batch_size=1, num_workers=0)

        inferences = {}
        with tqdm(THRESHOLDS) as pbar:
            for thresh in pbar:
                pbar.set_description(f"Threshold = {thresh}")
                threshold_inferences = {}
                for seed in SEEDS:
                    model_path = download_model(thresh, seed)
                    clf = MLP_C2H2(1024, 256, 128)
                    state_dict = safe_torch_load(model_path)['state_dict']
                    for key in list(state_dict.keys()):
                        state_dict[key.replace('model.model.', 'model.')] = state_dict.pop(key)
                    clf.load_state_dict(state_dict)
                    clf.eval()
                    device = "cuda" if int(args.GPUs) > 0 else "cpu"
                    clf.to(device)
                    threshold_inferences[seed] = inference_epoch(clf, emb_loader, device=device)

                for seq in threshold_inferences["1"].keys():
                    mean_prediction = sum(threshold_inferences[seed][seq] for seed in SEEDS) / len(SEEDS)
                    binary_pred = round(mean_prediction)
                    inferences[f"{seq}$%#{thresh}"] = (mean_prediction, binary_pred)
        inference_df = pd.DataFrame.from_dict(inferences, orient="index", columns=("Mean_Pred", "Binary_Pred"))
        inference_df = inference_df.reset_index(names="RawLab")
        split_values = inference_df["RawLab"].apply(lambda x: re.split(r"\$%#", x, maxsplit=1))
        if all(len(x) == 2 for x in split_values):
            inference_df["Protein"] = [x[0] for x in split_values]
            inference_df["Threshold"] = [x[1] for x in split_values]
        else:
            print("ERROR: Some rows did not split correctly.")
            failed_rows = [x for x in split_values if len(x) != 2]
            print("Rows that failed split:", failed_rows[:10])  # Show first few problem cases


        # inference_df[["Protein", "Threshold"]] = inference_df["RawLab"].str.split("$%#", expand=True)
        inference_df = inference_df.drop(columns="RawLab")[["Protein", "Threshold", "Mean_Pred", "Binary_Pred"]]
        inference_df.to_csv(os.path.join(args.outdir, f"{args.name}_TemStaPro_preds.csv"), index=False)
        
        if not args.save_emb and not args.preComputed_Embs:
            os.remove(os.path.join(args.outdir, f"{args.name}_ProtT5_AVG.csv"))
            
    elif args.classifier == "EpHod":
        logging.getLogger("pytorch_lightning.utilities.rank_zero").addHandler(logging.NullHandler())
        logging.getLogger("pytorch_lightning.accelerators.cuda").addHandler(logging.NullHandler())
        if not os.path.exists(os.path.join(cache_dir, "EpHod_Models")):
            logger.info("Downloading EpHod models...")
            cmd = ("curl", "-o", "saved_models.tar.gz", "--progress-bar",
                   "https://zenodo.org/records/8011249/files/saved_models.tar.gz?download=1")
            result = subprocess.run(cmd)

            shutil.move("saved_models.tar.gz", cache_dir)
            tarfile = os.path.join(cache_dir, "saved_models.tar.gz")
            shutil.unpack_archive(tarfile, cache_dir)
            os.remove(tarfile)
            shutil.move(os.path.join(cache_dir, "saved_models"), os.path.join(cache_dir, "EpHod_Models"))

        headers, sequences = eu.read_fasta(args.query)
        accessions = [head.split()[0] for head in headers]
        headers, sequences, accessions = [np.array(item) for item in (headers, sequences, accessions)]
        assert len(accessions) == len(headers) == len(sequences), "Fasta file has unequal headers and sequences"
        numseqs = len(sequences)

        # Check sequence lengths
        lengths = np.array([len(seq) for seq in sequences])
        long_count = np.sum(lengths > 1022)
        warning = f"{long_count} sequences are longer than 1022 residues and will be omitted"

        # Omit sequences longer than 1022
        if max(lengths) > 1022:
            logger.warning(warning)
            locs = np.argwhere(lengths <= 1022).flatten()
            headers, sequences, accessions = [array[locs] for array in (headers, sequences, accessions)]
            numseqs = len(sequences)

        if not os.path.exists(args.outdir):
            os.makedirs(args.outdir)

        # Prediction output file
        phout_file = os.path.join(args.outdir, f"{args.name}_EpHod.csv")
        embed_file = os.path.join(args.outdir, f"{args.name}_ESM1v_embeddings.csv")
        ephod_model = eu.EpHodModel(args)
        num_batches = int(np.ceil(numseqs / args.batch_size_emb))
        all_ypred, all_emb_ephod = [], []
        batches = range(1, num_batches + 1)
        batches = tqdm(batches, desc="Predicting pHopt")
        for batch_step in batches:
            start_idx = (batch_step - 1) * args.batch_size_emb
            stop_idx = batch_step * args.batch_size_emb
            accs = accessions[start_idx: stop_idx]
            seqs = sequences[start_idx: stop_idx]

            # Predict with EpHod model
            ypred, emb_ephod, attention_weights = ephod_model.batch_predict(accs, seqs, args)
            all_ypred.extend(ypred.to("cpu").detach().numpy())
            all_emb_ephod.extend(emb_ephod.to("cpu").detach().numpy())

        if args.save_emb:
            all_emb_ephod = pd.DataFrame(np.array(all_emb_ephod), index=accessions)
            all_emb_ephod.to_csv(embed_file)

        all_ypred = pd.DataFrame(all_ypred, index=accessions, columns=["pHopt"])
        all_ypred = all_ypred.reset_index(drop=False)
        all_ypred.rename(columns={"index": "Label"}, inplace=True)
        all_ypred.to_csv(phout_file, index=False)

    elif args.classifier == 'ESM2+MLP':
        if not args.preTrained:
            command_line_args = sys.argv
            command_line_str = " ".join(command_line_args)
            outfile = os.path.join(args.outdir, f"{args.name}_{args.classifier}_{args.emb_model}.out")
            logger.info("Prepping data for training ESM2+MLP...")
            train_df, test_df, n_classes, le = prep_hf_data(args)
            logger.info("Setting up ESM2+MLP...")
            trainer, test_dataset = setup_esm2_hf(train_df, test_df, args, n_classes)
            train_res = trainer.train()
            test_res = trainer.predict(test_dataset = test_dataset)
            trainer.model.save_pretrained(os.path.join(args.outdir, f'{args.name}_{args.emb_model}-MLP_{n_classes}-classifier.pt'), safe_serialization=False) 
            preds = np.argmax(test_res[0], axis=1)
            transformed_preds = le.inverse_transform(preds)
            unique_c = np.unique(transformed_preds)
            label_order = np.unique(test_df['NewLab'])
            precision, recall, fscore, support = precision_recall_fscore_support(test_df['NewLab'].values, preds, average=args.f1_avg_method, labels=np.unique(test_df['NewLab']))
            log_results(outfile, command_line_str, n_classes, args, classes=unique_c, precision=precision, recall=recall, fscore=fscore, support=support, le=le, LabelOrder=label_order)
        else:
            trainer, dataset, label_list = custom_esm2mlp_test(args)
            test_res = trainer.predict(test_dataset=dataset)
            # Convert probabilities to a DataFrame
            proba_df = pd.DataFrame(test_res[0])
            
            # Find the index of the maximum probability for each row (prediction)
            test_preds = proba_df.idxmax(axis=1)
            
            # Add the original labels to the DataFrame
            proba_df['Label'] = label_list
            
            # Save the probabilities to a CSV file
            proba_file_name = f'{args.name}_ESM2-MLP_class_probs.csv'
            proba_df.to_csv(os.path.join(args.outdir, proba_file_name), index=False)
            
            # Prepare and save the predictions to a CSV file
            pred_df = pd.DataFrame(test_preds, columns=['Prediction'])
            pred_df['Label'] = label_list
            
            pred_file_name = f'{args.name}_ESM2-MLP_predictions.csv'
            pred_df.to_csv(os.path.join(args.outdir, pred_file_name), index=False)


    elif args.classifier not in ['3Di-Search','ECPICK', 'iForest', 'PSALM', 'M-Ionic', 'CatPred', 'CataPro', 'PSICHIC', 'GraphEC']:
        outfile = os.path.join(args.outdir, f"{args.name}_{args.classifier}.out")
        if not args.preComputed_Embs:
            if not args.poolparti:
                embed_command = (
                    "trill",
                    args.name,
                    args.GPUs,
                    "--outdir", args.outdir,
                    "embed",
                    args.emb_model,
                    args.query,
                    "--avg",
                    "--batch_size",
                    str(args.batch_size_emb)
                )            
                subprocess.run(embed_command, check=True)
                df = pd.read_csv(os.path.join(args.outdir, f"{args.name}_{args.emb_model}_AVG.csv"))
            else:
                embed_command = (
                    "trill",
                    args.name,
                    args.GPUs,
                    "--outdir", args.outdir,
                    "embed",
                    args.emb_model,
                    args.query,
                    "--poolparti",
                    "--batch_size",
                    str(args.batch_size_emb)
                )
                subprocess.run(embed_command, check=True)
                df = pd.read_csv(os.path.join(args.outdir, f"{args.name}_{args.emb_model}_PoolParti.csv"))
        else:
            df = pd.read_csv(args.preComputed_Embs)

        if args.train_split is not None:
            le = LabelEncoder()
            train_df, test_df, n_classes = prep_data(df, args)
            train_df = train_df.dropna(subset=['NewLab'])
            test_df = test_df.dropna(subset=['NewLab'])
            unique_c = np.unique(test_df["NewLab"])
            classes = train_df["NewLab"].unique()
            train_df["NewLab"] = le.fit_transform(train_df["NewLab"])
            if not float(args.train_split) == 1.0:
                test_df["NewLab"] = le.transform(test_df["NewLab"])
            command_line_args = sys.argv
            command_line_str = " ".join(command_line_args)
            label_data = []
            for clas in classes:
                encoded_label = le.transform([clas])[0]
                label_data.append((encoded_label, clas))

            if args.sweep:
                sweeped_clf, study = sweep(train_df, test_df, args)
                if not float(args.train_split) == 1 or not float(args.train_split) == 1.0:
                    precision, recall, fscore, support, LabelOrder = predict_and_evaluate(sweeped_clf, le, test_df, args)
                    log_results(outfile, command_line_str, n_classes, args, classes=unique_c, sweeped_clf=sweeped_clf,precision=precision, recall=recall, fscore=fscore, support=support, le=le, LabelOrder=LabelOrder, study=study)
            else:
                if args.classifier == 'MLP':
                    if args.lr == 0.2:
                        args.lr = 0.0001
                    model = MLP_Classifier(input_size=len(train_df.columns)-2, hidden_layers=args.hidden_layers, dropout_rate=float(args.dropout), num_classes=len(unique_c), learning_rate=float(args.lr))
                    train_dataset = MLP_Emb_Dataset_train(train_df)
                    test_dataset = MLP_Emb_Dataset_train(test_df)
                    train_loader = DataLoader(train_dataset, shuffle=True, batch_size=int(args.batch_size_mlp), num_workers=0)
                    test_loader = DataLoader(test_dataset, shuffle=False, batch_size=int(args.batch_size_mlp), num_workers=0)
                    # print(train_df)
                    trainer = pl.Trainer(
                        max_epochs=int(args.epochs),
                        accelerator = 'gpu' if int(args.GPUs) != 0 else 'cpu',
                        devices=0 if int(args.GPUs) == 0 else int(args.GPUs),
                        # callbacks=[checkpoint_callback, rich_progress_bar],
                        deterministic=True,  # Ensure reproducibility
                        precision='16' if int(args.GPUs) != 0 else '32-true',
                        num_nodes=int(args.nodes),
                        check_val_every_n_epoch=1
                    )
                    trainer.fit(model, train_dataloaders = train_loader, val_dataloaders = test_loader)
                    trainer.save_checkpoint(os.path.join(args.outdir, f"{args.name}_{args.emb_model}_MLP_{args.epochs}.pt"))
                else:
                    clf = train_model(train_df, args)
                    clf.save_model(os.path.join(args.outdir, f"{args.name}_{args.classifier}_{len(train_df.columns) - 2}.json"))
                    if not float(args.train_split) == 1 or not float(args.train_split) == 1.0:
                        precision, recall, fscore, support, LabelOrder = predict_and_evaluate(clf, le, test_df, args)
                        log_results(outfile, command_line_str, n_classes, args, classes=classes, precision=precision,recall=recall, fscore=fscore, support=support, le=le, LabelOrder=LabelOrder)

            df = pd.DataFrame(label_data, columns=['EncodedLabel', 'OriginalLabel'])

            output_csv_path = os.path.join(args.outdir, f"{args.name}_{args.classifier}_prediction_class_key.csv")
            df.to_csv(output_csv_path, index=False)
            if not args.save_emb and not args.preComputed_Embs:
                os.remove(os.path.join(args.outdir, f"{args.name}_{args.emb_model}_AVG.csv"))
            logger.info(f'Saving prediction output key for this model at {output_csv_path}')

        elif args.classifier not in ['3Di-Search','ECPICK', 'PSALM', 'M-Ionic', 'CatPred', 'CataPro', 'PSICHIC', 'GraphEC']:
            if not args.preTrained:
                logger.error("You need to provide a model with --preTrained to perform inference!")
                raise Exception("You need to provide a model with --preTrained to perform inference!")
            elif args.classifier == 'MLP':
                model = MLP_Classifier()
                model = model.load_from_checkpoint(args.preTrained)
                test_dataset = MLP_Emb_Dataset_test(df)
                test_loader = DataLoader(test_dataset, shuffle=False, batch_size=int(args.batch_size_mlp), num_workers=0)
                trainer = pl.Trainer(
                    max_epochs=int(args.epochs),
                    accelerator = 'gpu' if int(args.GPUs) != 0 else 'cpu',
                    devices=0 if int(args.GPUs) == 0 else int(args.GPUs),
                    # callbacks=[checkpoint_callback, rich_progress_bar],
                    deterministic=True,  # Ensure reproducibility
                    precision='16' if int(args.GPUs) != 0 else '32-true',
                    num_nodes=int(args.nodes),
                    )
                preds = trainer.predict(model, test_loader)
                classifications = [torch.argmax(tensor).item() for tensor in preds]

                results = []

                # Loop through the labels and predictions, and append them to the results list
                for lab, pred in zip(df['Label'], classifications):
                    results.append({'Label': lab, 'Prediction': pred})

                results_df = pd.DataFrame(results)

                # Save the DataFrame to a CSV file
                results_df.to_csv(os.path.join(args.outdir, f'{args.name}_MLP_predictions.csv'), index=False)

            else:
                clf = load_model(args)
                custom_model_test(clf, df, args)

                if not args.save_emb and not args.preComputed_Embs:
                    os.remove(os.path.join(args.outdir, f"{args.name}_{args.emb_model}_AVG.csv"))

    elif args.classifier not in ['iForest','ECPICK','PSALM', 'M-Ionic', 'CatPred', 'CataPro', 'PSICHIC', 'GraphEC']:
        # Load embeddings
        if not args.preComputed_Embs:
            if not args.poolparti:
                embed_command = (
                    "trill",
                    args.name,
                    args.GPUs,
                    "--outdir", args.outdir,
                    "embed",
                    args.emb_model,
                    args.query,
                    "--avg",
                    "--batch_size",
                    str(args.batch_size_emb)
                )            
                subprocess.run(embed_command, check=True)
                df = pd.read_csv(os.path.join(args.outdir, f"{args.name}_{args.emb_model}_AVG.csv"))
            else:
                embed_command = (
                    "trill",
                    args.name,
                    args.GPUs,
                    "--outdir", args.outdir,
                    "embed",
                    args.emb_model,
                    args.query,
                    "--poolparti",
                    "--batch_size",
                    str(args.batch_size_emb)
                )
                subprocess.run(embed_command, check=True)
                df = pd.read_csv(os.path.join(args.outdir, f"{args.name}_{args.emb_model}_PoolParti.csv"))
        else:
            df = pd.read_csv(args.preComputed_Embs)

        # Filter fasta file
        if args.preComputed_Embs and not args.preTrained:
            valid_labels = set(df["Label"])
            filtered_records_labels = {record.id for record in SeqIO.parse(args.query, "fasta") if
                                       record.id in valid_labels}
            df = df[df["Label"].isin(filtered_records_labels)]

        # Train or load model
        if not args.preTrained:
            model = IsolationForest(
                random_state=int(args.RNG_seed),
                verbose=True,
                n_estimators=int(args.n_estimators),
                contamination=float(args.if_contamination) if args.if_contamination != "auto" else "auto"
            )
            model.fit(df.iloc[:, :-1])
            sio.dump(model, os.path.join(args.outdir, f"{args.name}_iForest.skops"))
        else:
            model = sio.load(args.preTrained, trusted=True)

            # Predict and output results
            preds = model.predict(df.iloc[:, :-1])
            # unique_values, counts = np.unique(preds, return_counts=True)
            # for value, count in zip(unique_values, counts):
            #     print(f"{value}: {count}")

            df["Predicted_Class"] = preds
            out_df = df[("Label", "Predicted_Class")]
            out_df.to_csv(os.path.join(args.outdir, f"{args.name}_iForest_predictions.csv"), index=False)
        if not args.save_emb and not args.preComputed_Embs:
            os.remove(os.path.join(args.outdir, f"{args.name}_{args.emb_model}_AVG.csv"))


    elif args.classifier == '3Di-Search':
        logger.info(f'Prepping Foldseek databases from {args.query} and {args.db}')
        query_preds_out_path, db_preds_out_path = get_3di_embeddings(args, cache_dir)
        prep_foldseek_dbs(args.query, query_preds_out_path, f'{args.name}_query')
        prep_foldseek_dbs(args.db, db_preds_out_path, f'{args.name}_db')
        logger.info(f'Finished creating Foldseek databases!')
        foldseek_search_cmd = f'foldseek search tmp_{args.name}_query_db tmp_{args.name}_db_db {args.name}_3di-search_results tmp -v 0'
        logger.info(f'Starting foldseek search with: \n{foldseek_search_cmd}')
        subprocess.run(foldseek_search_cmd.split())
        output_path = os.path.join(args.outdir, f'{args.name}_3di-search_results.tsv')
        foldseek_convertalis_cmd = f'foldseek convertalis tmp_{args.name}_query_db tmp_{args.name}_db_db {args.name}_3di-search_results {output_path} -v 0'.split()
        subprocess.run(foldseek_convertalis_cmd)
        logger.info(f'Foldseek output can be found at {output_path}!')

    elif args.classifier == "PSALM":
        og_biopython_ver, og_np_ver, pypar_ver = get_current_biopython_version()
        upgrade_biopython('1.83', og_np_ver, pypar_ver)
        try:
            pkg_resources.get_distribution("psalm")
        except pkg_resources.DistributionNotFound:
            install_cmd = "pip install protein-sequence-annotation".split(" ")
            subprocess.run(install_cmd)
        from psalm import psalm
        from psalm.viz_utils import plot_predictions
        outfile = os.path.join(args.outdir, f"{args.name}_{args.classifier}.out")
        if not args.preComputed_Embs:
            embed_command = (
                "trill",
                args.name,
                args.GPUs,
                "--outdir", args.outdir,
                "embed",
                "esm2_t33_650M",
                args.query,
                "--per_AA"
            )
            logger.info("Extracting embeddings from ESM2-650M...")
            subprocess.run(embed_command, check=True)
            perAA = safe_torch_load(os.path.join(args.outdir, f"{args.name}_esm2_t33_650M_perAA.pt"), weights_only=False)
        else:
            perAA = safe_torch_load(args.preComputed_Embs, weights_only=False)
        device = 'cuda' if int(args.GPUs) > 0 else 'cpu'
        PSALM = psalm(clan_model_name="ProteinSequenceAnnotation/PSALM-1b-clan",
                    fam_model_name="ProteinSequenceAnnotation/PSALM-1b-family",
                    device = device)  


        # embeddings = [emb for emb, label in perAA[0]]
        # labels = [label for emb, label in perAA[0]]
        data = [emb for emb, label in perAA]
        embeddings = []
        labels = []
        for tup in data:
            embeddings.append(tup[0])
            labels.append(tup[1])

        max_length = max([emb.shape[0] for emb in embeddings])

        # Initialize DataFrames with NaN values
        fam_aa_df = pd.DataFrame(columns=range(max_length))
        clan_aa_df = pd.DataFrame(columns=range(max_length))

        with open(os.path.join(args.outdir, f'{args.name}_{args.classifier}_preds.csv'), 'w') as outcsv:

            outcsv.write('Label,Families,Clans\n')
            logger.info("Using ESM2 embeddings for PSALM predictions...")

            for i, (emb, lab) in tqdm(enumerate(zip(embeddings, labels)), total=len(embeddings), desc="Performing PSALM predictions"):
                # fixed = emb[1:len(emb), :]
                fixed = torch.tensor(emb)
                mask = torch.ones(len(fixed), dtype=torch.bool)
                mask = mask.to(device)
                mask = mask.unsqueeze(-1)
                # clan_preds = PSALM.clan_model(fixed.to(device))
                fixed = fixed.unsqueeze(0)
                mask = mask.transpose(0, 1)
                clan_logits = PSALM.clan_model(fixed.to(device), mask.to(device))
                clan_preds = F.softmax(clan_logits, dim=2)
                # fam_preds = PSALM.fam_model(fixed.to(device), clan_preds, PSALM.clan_fam_matrix)
                fam_preds, fam_logits = PSALM.fam_model(fixed.to(device), mask, clan_preds)
                for i in range(PSALM.clan_fam_matrix.shape[0]):  # shape is cxf
                    indices = torch.nonzero(PSALM.clan_fam_matrix[i]).squeeze()
                    if i == PSALM.clan_fam_matrix.shape[0] - 1:
                        fam_preds[:, :, indices] = 1  # IDR is 1:1 map
                    else:
                        fam_preds[:, :, indices] = F.softmax(fam_preds[:, :, indices], dim=2)
                clan_preds_f = torch.matmul(clan_preds, PSALM.clan_fam_matrix)
                fam_preds = fam_preds * clan_preds_f
                clan_preds = clan_preds.squeeze(0)
                fam_preds = fam_preds.squeeze(0)
                # with patch('matplotlib.pyplot.show', new=noop):
                #     plot_predictions(fam_preds.detach().cpu(), clan_preds.detach().cpu(), PSALM.fam_maps, 0.72, seq_name=lab, save_path=args.outdir)
            

                fam_top_val, fam_top_index = torch.topk(fam_preds,k=1,dim=1)
                unique_fam_values = torch.unique(fam_top_index)
                num_unique_fam_values = unique_fam_values.numel()

                clan_top_val, clan_top_index = torch.topk(clan_preds, k=1, dim=1)
                unique_clan_values = torch.unique(clan_top_index)
                num_unique_clan_values = unique_clan_values.numel()

                fam_keys = PSALM.fam_maps['idx_fam']
                clan_keys = PSALM.fam_maps['idx_clan']

                fam_pred_labels = fam_top_index
                fam_pred_vals = fam_top_val
                clan_pred_labels = clan_top_index
                clan_pred_vals = clan_top_val
                fam_unique_test = torch.unique(fam_pred_labels)
                clan_unique_test = torch.unique(clan_pred_labels)
                if fam_unique_test[-1] == 19632:
                    fam_unique_test = fam_unique_test[:-1]
                if clan_unique_test[-1] == 656:
                    clan_unique_test = clan_unique_test[:-1]
                fams = []
                for entry in fam_unique_test:
                    idx = (fam_pred_labels == entry) & (fam_pred_vals >= 0.72)
                    fams.append(fam_keys[entry.item()].split(".")[0])
                    residues = torch.where(idx)[0]
                    for residue in residues.cpu().numpy():
                        fam_aa_df.loc[lab, residue] = f"{fam_keys[entry.item()].split('.')[0]}:{fam_pred_vals[idx][residues == residue].item()}"

                clans = []
                for entry in clan_unique_test:
                    idx = (clan_pred_labels == entry) & (clan_pred_vals >= 0.72)
                    if torch.count_nonzero(idx) != 0:
                        clans.append(clan_keys[entry.item()].split(".")[0])
                        residues = torch.where(idx)[0]
                        for residue in residues.cpu().numpy():
                            clan_aa_df.loc[lab, residue] = f"{clan_keys[entry.item()].split('.')[0]}:{clan_pred_vals[idx][residues == residue].item()}"


                clans = [x.replace("NC0001", "Non-Clan") for x in clans]

                outcsv.write(f'{lab},{":".join(fams)},{":".join(clans)}\n')

        fam_aa_df.to_csv(os.path.join(args.outdir, f'{args.name}_{args.classifier}_pfam_AA_preds.csv'), index=True)
        clan_aa_df.to_csv(os.path.join(args.outdir, f'{args.name}_{args.classifier}_clan_AA_preds.csv'), index=True)
        upgrade_biopython(og_biopython_ver, og_np_ver, pypar_ver)
